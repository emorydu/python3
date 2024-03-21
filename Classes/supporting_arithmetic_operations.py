class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, rhs):
        return self.x + rhs.x, self.y + rhs.y


point = Point(10, 20)
other = Point(1, 2)
print(point + other)