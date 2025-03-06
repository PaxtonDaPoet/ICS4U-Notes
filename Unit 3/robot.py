class Robot:

    def __init__(self,position, direction):

        if direction == "RIGHT":
            self.position = position
        elif direction == "LEFT":
            self.position = -1*position
        else:
            print("Invalid direction, POSITION = HOME BASE")
            self.position = 0

        self.speed = 0

    def moveRight(self, time):
        if self.speed == 0:
            print("Set Speed Before Moving")
        else:
            self.position = self.position + self.speed * time

    def moveLeft(self, time):
        if self.speed == 0:
            print("Set Speed Before Moving")
        else:
            self.position = self.position - self.speed * time

    def changeSpeed(self,amount):
        if self.speed + amount < 0:
            self.speed = 0
        elif self.speed + amount > 30:
            self.speed = 30
        else:
            self.speed = self.speed + amount

    def __str__(self):
        if self.position == 0:
            return "At Home Base"
        elif self.position > 0:
            return str(self.position) + "cm RIGHT of Home Base"
        else:
            return str(self.position) + "cm LEFT of Home Base"  