from snake import Snake
import random

'''
To use the Template:
1. Change this file name `MySnakeTemplate.py` to your own/nick name
2. Change this class name `MySnakeTemplate` to your own/nick name
3. Implement the TODO sections
'''
class MySnakeTemplate3(Snake):
    def __init__(self):
        # TODO: Construct your snake
        # start_x, start_y should be your assigned starting position.
        # length + attack + hp should be added up to a maximum of 10; otherwise, the snake will be disqualified and removed from the game.
        super().__init__(30, 15, (0,0,255), 'MySnakeTemplate3', 150, 10, 20)

    def move(self) -> None:
        # TODO: Write your own find next moving direction logic
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        direction = random.choice(direction)

        return super().move(direction)

    # [OPTIONAL]
    def detect(self, map : list[list[list]]) -> None:
        # TODO:  You can utilize the detect feature called every round
        #        to store any value that's helpfull for your move() direction logic
        # NOTE:
        #   1. ONLY allow to have a MAXIMUM runtine of 1 second!
        #   2. STORE any information as ATTRIBUTES.
        #   3. DO NOT return anything
        super().detect(map) # Do nothing

    def _checkCollision(self) -> bool:
        # TODO: [OPTIONAL] Write a helper method to check if the snake would collide with the wall
        return None

    def _getPosition(self) -> tuple[int, int]:
        # TODO: Write a helper method to get the current head position of the snake
        return None