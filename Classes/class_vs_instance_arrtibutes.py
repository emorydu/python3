class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.default_color)
point.z = 10
Point.default_color = "yellow"

print(point.x)
print(point.y)
point.draw()
print(point.z)

another = Point(3, 4)
print(another.default_color)
another.draw()
print(another.x, another.y)
