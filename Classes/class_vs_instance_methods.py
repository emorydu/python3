class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return f"Point ({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)    # cls(0, 0) == Point(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()
