class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
point.draw()
print(isinstance(point, Point))

