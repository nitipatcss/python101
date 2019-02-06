"""
Square     : w ** 2
Rectangle  : w * h
Triangle   : 1 / 2 * w * h
Circle     : Pi * r ** :2
"""

#
# def Rectangle(width, height):
#     return width * height
from shape import shape


class Rectangle(shape):
    name = "Rectangle instance with area : "

    def __str__(self) -> str:
        return self.name + str(self.width * self.height)


class Triangle(shape):
    name = "Triangle instance with area : "

    def area(self):
        return 1 / 2 * self.width * self.height

    def __str__(self) -> str:
        return self.name + str(1 / 2 * self.width * self.height)


if __name__ == '__main__':
    r = Rectangle(25, 15)
    print(r)
    print("My rectangle area is : " + str(r.area()))

    t = Triangle(10, 25)
    print(t)
    print("My triangle area is : " + str(t.area()))
