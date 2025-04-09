from snake import Snake
import random

'''
To use the Template:
1. Change this file name `MySnakeTemplate.py` to your own/nick name
2. Change this class name `MySnakeTemplate` to your own/nick name
3. Implement the TODO sections
'''
class BlueSnake(Snake):
    def __init__(self):
        # Dynamically calculate initial position based on MATRIX_SIZE
        self.x = 0  # Start at the leftmost position (x=0)
        self.y = Snake.MATRIX_SIZE[1] - 1  # Start at the bottom row (y=MATRIX_SIZE[1] - 1)
        
        color = (0, 0, 255)  # Blue color
        name = "BlueSnake"
        
        # Assign stats ensuring length + atk + hp = 200
        length = 100
        atk = 50
        hp = 50
        
        super().__init__(self.x, self.y, color, name, length, atk, hp)
        
        # Snake's body is a list of tuples, starting with the head
        self.body = [(self.x, self.y)]
    
    def move(self) -> None:
    # Define movement directions: Up, Right (to move away from bottom-left)
        direction = random.choice([[0, -1], [1, 0],[-1,0],[0,1]])  # Move up or right and down or left
    # Check if the chosen direction causes a collision
        while self._checkCollision(direction):
            direction = random.choice([[0, -1], [1, 0],[-1,0],[0,1]]) 
        return direction  # Stop movement if there's a collision
      
    def detect(self, map: list[list[list]]) -> None:
        # Optional: Implement logic to analyze the map before moving
        self.map_data = map  # Store map data if needed
    
    def _checkCollision(self, direction: tuple[int, int]) -> bool:
    
    # Get the current head position (first element in the body)
        head_x, head_y = self.body[0]  # Unpack the x and y values of the head
    
    # Calculate the next position based on the direction
        next_x = head_x + direction[0]
        next_y = head_y + direction[1]
    
    # Check collision with walls (assuming the map is dynamically sized)
        if next_x < 0 or next_x >= Snake.MATRIX_SIZE[0] or next_y < 0 or next_y >= Snake.MATRIX_SIZE[1]:\
            return True  # Collided with a wall

    # Check collision with itself (if there's a body list and positions are tracked)    
        if (next_x, next_y) in self.body:
            return True  # Collided with itself

        return False  # No collision

    def _getPosition(self) -> tuple[int, int]:
        """Return the snake's current position, which is the head of the body."""
        head_x, head_y = self.body[0]
        return head_x, head_y
    def get_y(self) -> int:
        return self.body[0][1]
def main():
    # Initialize the snake
    snake = BlueSnake()
    print(snake)

    # Grow the snake
    snake.grow()
    snake.grow()
    snake.grow()
    print(snake)

    # Move the snake multiple times
    for _ in range(7):
        snake.move()
        print(snake)

main()
