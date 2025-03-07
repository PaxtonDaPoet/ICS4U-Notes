# Inheritance
## class child(Parent)
class Human:
    def __init__(self, hp, x, y):
        self.hp = hp
        self.position = [x, y]

    def move(self, direction: list[int, int]) -> None:
        self.position = direction

    def moveXY(self, x: int, y: int) -> None:
        self.move([x, y])

    @classmethod
    def getSpecious(cls):
        return "human"
