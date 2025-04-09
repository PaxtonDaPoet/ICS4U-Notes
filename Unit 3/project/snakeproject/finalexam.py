class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius 
    def area(self):
        return 3.14159 * self.radius ** 2
    def __str__(self):
        return f"Circle(center={super().__str__()}, radius={self.radius})"

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height
    def volume(self):
        return self.area() * self.height
    def __str__(self):
        return f"Cylinder(base={super().__str__()}, height={self.height})"
p = Point(2, 3)
print(p)

c = Circle(5, 5, 10)
print(c)
print("Area:", c.area())

cyl = Cylinder(0, 0, 5, 10)
print(cyl)
print("Volume:", cyl.volume())