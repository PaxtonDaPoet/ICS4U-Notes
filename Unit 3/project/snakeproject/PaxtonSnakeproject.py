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
    # List of potential movement directions (up, right, left, down)
        directions = [[0, -1], [1, 0], [-1, 0], [0, 1]]

    # Randomly shuffle the directions to randomize the choices
        random.shuffle(directions)

    # Try all shuffled directions until a valid one is found
        for direction in directions:
            if not self._checkCollision(direction):
            # If no collision, move the snake in the valid direction
                super().move(direction)
            print(f"Moved in direction: {direction}")  # Print the movement
            return direction  # Return the valid direction immediately after moving
    
    # If no valid move is found (all directions are blocked), do nothing or handle accordingly
        print("No valid move found.")
        return None  # Return None if no valid move is possible


    
    def _checkCollision(self, direction: tuple[int, int]) -> bool:
        head_x, head_y, hp = self.body_positions[0]  # Unpack x, y, and hp from the head
        
        next_x = head_x + direction[0]
        next_y = head_y + direction[1]
        
        # Check for boundary collisions
        if next_x < 0 or next_x >= Snake.MATRIX_SIZE[0] or next_y < 0 or next_y >= Snake.MATRIX_SIZE[1]:
            return True
        
        # Check for self-collision (if the next position is already occupied by the snake's body)
        if (next_x, next_y) in [(body[0], body[1]) for body in self.body_positions[1:]]:
            return True
        
        return False
    
    def _getPosition(self) -> tuple[int, int]:
        return self.body_positions[0][:2]  # Return only the x, y position (head)
    
    def get_y(self) -> int:
        return self.body_positions[0][1]  # Access the y-coordinate of the head only

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
