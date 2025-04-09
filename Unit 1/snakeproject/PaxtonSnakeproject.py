from snake import Snake
import random
from typing import List

class BlueSnake(Snake):
    def __init__(self):
        start_x = 0  # Start at the leftmost position (x=0)
        start_y = Snake.MATRIX_SIZE[1] - 1  # Start at the bottom row (y=MATRIX_SIZE[1] - 1)
        
        color = (0, 0, 255)  # Blue color
        name = "BlueSnake"
        length = 100
        atk = 50
        hp = 50
        super().__init__(start_x, start_y, color, name, length, atk, hp)
        self.last_direction = [1, 0]  # Default to moving right initially
        self.vision_range = 5  # How many squares away it can detect other snakes
    
    def move(self, snakes: List[Snake], foods: List[tuple]) -> None:
        # Get current position
        head_x, head_y = self._getPosition()
        
        # Analyze environment
        enemies = self._detect_enemies(snakes)
        threats = self._identify_threats(enemies)
        targets = self._identify_targets(enemies)
        nearest_food = self._find_nearest_food(foods)
        
        # Decision making
        if threats:
            # Evade the most dangerous threat
            best_escape = self._find_escape_route(threats)
            if best_escape:
                super().move(best_escape)
                self.last_direction = best_escape
                print(f"Evading threat by moving {best_escape}")
                return
        
        if targets:
            # Attack the weakest target
            best_attack = self._find_attack_route(targets)
            if best_attack:
                super().move(best_attack)
                self.last_direction = best_attack
                print(f"Attacking target by moving {best_attack}")
                return
        
        if nearest_food:
            # Move toward food if no immediate threats or targets
            food_dir = self._direction_toward(nearest_food)
            if not self._checkCollision(food_dir):
                super().move(food_dir)
                self.last_direction = food_dir
                print(f"Moving toward food at {nearest_food}")
                return
        
        # Default movement if no special cases
        self._default_movement()
    
    def _default_movement(self):
        # Try to continue in the same direction if possible
        if not self._checkCollision(self.last_direction):
            super().move(self.last_direction)
            print(f"Continuing in direction: {self.last_direction}")
            return

        # If can't continue, try random directions
        directions = [
            [0, -1],  # up
            [1, 0],   # right
            [-1, 0],  # left
            [0, 1]    # down
        ]
        random.shuffle(directions)
        
        for direction in directions:
            if not self._checkCollision(direction):
                super().move(direction)
                self.last_direction = direction
                print(f"Changed to direction: {direction}")
                return

        # If completely stuck, don't move
        print("Completely stuck - cannot move")
    
    def _detect_enemies(self, snakes: List[Snake]) -> List[Snake]:
        """Return list of other snakes within vision range"""
        head_x, head_y = self._getPosition()
        enemies = []
        
        for snake in snakes:
            if snake is not self:  # Don't detect self
                snake_x, snake_y = snake.body_positions[0]
                distance = abs(snake_x - head_x) + abs(snake_y - head_y)
                if distance <= self.vision_range:
                    enemies.append(snake)
        
        return enemies
    
    def _identify_threats(self, enemies: List[Snake]) -> List[Snake]:
        """Return list of snakes that are stronger than us"""
        threats = []
        for enemy in enemies:
            # Consider enemy a threat if they have higher ATK or similar ATK but longer length
            if enemy.atk > self.atk or (enemy.atk == self.atk and enemy.length > self.length):
                threats.append(enemy)
        return threats
    
    def _identify_targets(self, enemies: List[Snake]) -> List[Snake]:
        """Return list of snakes that are weaker than us"""
        targets = []
        for enemy in enemies:
            # Consider enemy a target if we have higher ATK or similar ATK but longer length
            if self.atk > enemy.atk or (self.atk == enemy.atk and self.length > enemy.length):
                targets.append(enemy)
        return targets
    
    def _find_nearest_food(self, foods: List[tuple]) -> tuple:
        """Return position of nearest food item"""
        if not foods:
            return None
            
        head_x, head_y = self._getPosition()
        nearest = None
        min_distance = float('inf')
        
        for food in foods:
            fx, fy = food
            distance = abs(fx - head_x) + abs(fy - head_y)
            if distance < min_distance:
                min_distance = distance
                nearest = food
                
        return nearest
    
    def _find_escape_route(self, threats: List[Snake]) -> list:
        """Find best direction to move away from threats"""
        if not threats:
            return None
            
        head_x, head_y = self._getPosition()
        
        # Calculate danger direction (weighted average of threat positions)
        danger_x, danger_y = 0, 0
        total_weight = 0
        
        for threat in threats:
            tx, ty = threat.body_positions[0]
            weight = threat.atk * threat.length  # Stronger/longer snakes are more dangerous
            danger_x += (tx - head_x) * weight
            danger_y += (ty - head_y) * weight
            total_weight += weight
        
        if total_weight > 0:
            danger_x /= total_weight
            danger_y /= total_weight
        
        # We want to move in the opposite direction of the danger
        escape_directions = []
        
        if danger_x > 0:
            escape_directions.append([-1, 0])  # left
        elif danger_x < 0:
            escape_directions.append([1, 0])   # right
            
        if danger_y > 0:
            escape_directions.append([0, -1])  # up
        elif danger_y < 0:
            escape_directions.append([0, 1])   # down
            
        # Try escape directions in order of preference
        for direction in escape_directions:
            if not self._checkCollision(direction):
                return direction
                
        # If can't escape directly away, try any safe direction
        directions = [
            [0, -1], [1, 0], [-1, 0], [0, 1]  # up, right, left, down
        ]
        random.shuffle(directions)
        
        for direction in directions:
            if not self._checkCollision(direction):
                return direction
                
        return None
    
    def _find_attack_route(self, targets: List[Snake]) -> list:
        """Find best direction to move toward weakest target"""
        if not targets:
            return None
            
        # Find the weakest target (lowest ATK and HP)
        weakest = min(targets, key=lambda x: (x.atk, x.hp))
        tx, ty = weakest.body_positions[0]
        
        return self._direction_toward((tx, ty))
    
    def _direction_toward(self, position: tuple) -> list:
        """Find best direction to move toward a position"""
        head_x, head_y = self._getPosition()
        target_x, target_y = position
        
        preferred_directions = []
        
        if target_x > head_x:
            preferred_directions.append([1, 0])  # right
        elif target_x < head_x:
            preferred_directions.append([-1, 0])  # left
            
        if target_y > head_y:
            preferred_directions.append([0, 1])  # down
        elif target_y < head_y:
            preferred_directions.append([0, -1])  # up
            
        # Try preferred directions first
        for direction in preferred_directions:
            if not self._checkCollision(direction):
                return direction
                
        # If can't move directly toward, try any safe direction
        directions = [
            [0, -1], [1, 0], [-1, 0], [0, 1]  # up, right, left, down
        ]
        random.shuffle(directions)
        
        for direction in directions:
            if not self._checkCollision(direction):
                return direction
                
        return None
    
    def _checkCollision(self, direction: list[int, int]) -> bool:
        head_x, head_y = self._getPosition()
        next_x = head_x + direction[0]
        next_y = head_y + direction[1]
        
        # Check boundaries
        if (next_x < 0 or next_x >= Snake.MATRIX_SIZE[0] or 
            next_y < 0 or next_y >= Snake.MATRIX_SIZE[1]):
            return True
        
        # Check self-collision (skip head)
        for segment in self.body_positions[1:]:
            if next_x == segment[0] and next_y == segment[1]:
                return True
        
        return False
    
    def _getPosition(self) -> tuple[int, int]:
        return (self.body_positions[0][0], self.body_positions[0][1])
    
    def get_y(self) -> int:
        return self.body_positions[0][1]

def main():
    from snake import Snake  # Assuming Snake is the base class
    
    # Create some test snakes
    blue_snake = BlueSnake()
    red_snake = Snake(5, 5, (255, 0, 0), "RedSnake", 50, 30, 40)  # Weaker than blue
    green_snake = Snake(10, 10, (0, 255, 0), "GreenSnake", 120, 60, 80)  # Stronger than blue
    
    # Create some test food
    foods = [(2, 2), (8, 8), (15, 15)]
    
    # Test movement with other snakes and food
    for i in range(20):
        snakes = [blue_snake, red_snake, green_snake]
        blue_snake.move(snakes, foods)
        print(f"After move {i+1}:")
        print(blue_snake)

if __name__ == "__main__":
    main()