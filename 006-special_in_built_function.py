class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(x={0}, y={1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


first_point = Point(1, 3)
print(first_point)
second_point = Point(2, 1)
print(second_point + first_point)