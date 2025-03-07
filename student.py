from human import human 
class Student(humanuman):  # Fixed class definition
    '''Student class inherits from Human class'''
    def __init__(self, hp, x, y, grade_level, GPA):
        super().__init__(hp, x, y)
        self.grade_level = grade_level
        self.GPA = GPA

    def move(self, direction: list[int, int]) -> None:
        dir = [direction[0] * 5, direction[1] * 5]
        super().move(dir)

    def getHuman(self):  # Override to include student info
        return f"HP: {self.hp}, Position: {self.position}, Grade: {self.grade_level}, GPA: {self.GPA}"