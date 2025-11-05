
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        print("circle",self.radius ** 2 * 3.14)

class Square(Shape):
    def __init__(self, a):
        self.square = a

    def area(self):
        print("Square",self.square * self.square)
