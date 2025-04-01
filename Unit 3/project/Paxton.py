from snake import Snake
import random

class BlueSnake(Snake):
    def __init__(self):
        self.x = 0  # Start at the leftmost position (x=0)
        self.y = Snake.MATRIX_SIZE[1] - 1  # Start at the bottom row (y=MATRIX_SIZE[1] - 1)
        
        color = (0, 0, 255)  # Blue color
        name = "BlueSnake"
        
        length = 100
        atk = 50
        hp = 50
        
        super().__init__(self.x, self.y, color, name, length, atk, hp)
    
    def move(self) -> None:
        # Pick a random direction
        direction = random.choice([[0, -1], [1, 0], [-1, 0], [0, 1]])  
        
        # Check for valid direction
        while self._checkCollision(direction):
            direction = random.choice([[0, -1], [1, 0], [-1, 0], [0, 1]])
        
        # If the snake doesn't collide, move it
        super().move(direction)
    
    def detect(self, map: list[list[list]]) -> None:
        self.map_data = map  # Store the map data, can be used for further logic
    
    def _checkCollision(self, direction: tuple[int, int]) -> bool:
        # Only unpack x, y coordinates from body_positions
        head_x, head_y = self.body_positions[0][:2]
        
        next_x = head_x + direction[0]
        next_y = head_y + direction[1]
        
        # Check for boundary collisions
        if next_x < 0 or next_x >= Snake.MATRIX_SIZE[0] or next_y < 0 or next_y >= Snake.MATRIX_SIZE[1]:
            return True
        
        # Check for self-collision
        if (next_x, next_y) in [body[:2] for body in self.body_positions[1:]]:
            return True
        
        return False
    
    def _getPosition(self) -> tuple[int, int]:
        return self.body_positions[0][:2]  # Return only x, y position
    
    def get_y(self) -> int:
        return self.body_positions[0][1]  # Access the y coordinate only

def main():
    snake = BlueSnake()
    print(snake)

    # Grow the snake by 3 units
    snake.grow()
    snake.grow()
    snake.grow()
    print(snake)

    # Move the snake 7 times
    for _ in range(7):
        snake.move()
        print(snake)

if __name__ == "__main__":
    main()
