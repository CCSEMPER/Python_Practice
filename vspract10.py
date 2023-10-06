from graphics import *

class MyPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x()

    def getY(self):
        return self.y()

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        output = "MyPoint({0},{1})".format(self.x, self.y)
        return output

    def draw(self, win):
        point = Point(self.x, self.y)
        point.draw(win)


def testMyPoint():
    myPoint = MyPoint(100,50)
    print(myPoint.getX)
    print(myPoint.getY)
    myPoint.move(10,20)
    print(myPoint.getX())
    print(myPoint.getY())
    print(myPoint)

testMyPoint()