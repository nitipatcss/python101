"""
Square     : w ** 2
Rectangle  : w * h
Triangle   : 1 / 2 * w * h
Circle     : Pi * r ** :2
"""
#
# def Rectangle(width, height):
#     return width * height

class Rectangle(object):
    name = "Rectangle instance with area : "

    def __init__(self, w, h):
        # width and height when use in class
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __str__(self):
        return self.name + str(self.width * self.height)


if __name__ == '__main__':
    r = Rectangle(25, 15)
    print(r)
    print("My rectangle area is : " + str(r.area()))
