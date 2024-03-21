class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def __gt__(self, rhs):
        return self.x > rhs.x and self.y > rhs.y

    def __lt__(self, rhs):
        return self.x < rhs.x and self.y < rhs.y

    def __ge__(self, rhs):
        return self.x >= rhs.x and self.y >= rhs.y

    def __le__(self, rhs):
        return self.x <= rhs.x and self.y <= rhs.y

    
point = Point(1, 2)
other = Point(1, 2)
print(point == other)
print(point > other)
print(point < other)
print(point >= other)
print(point <= other)

