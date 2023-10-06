from graphics import *


# Write your code here
# Not sure where to start?
# Check out README.md under "Files"

def tenColouredRectangles():
    win = GraphWin("Coloured Rectangles")
    message = Text(Point(100, 120), "Enter colour of the box ")
    message.draw(win)
    inputBox = Entry(Point(80, 20), 10)
    inputBox.draw(win)
    win.getMouse

    for i in range(10):
        message = Text(Point(100, 100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        rectangle = Rectangle (p1, p2)
        #text = Text(Point(150,15), colour)
        #text.draw(win) (if the entry is a string)
        rectangle.draw(win)
        colour = inputBox.getText()
        rectangle.setFill(colour)

        #colour = input("What colour is the rectangle? ")
        #rectangle.setFill(colour)


def tenStrings():
  win = GraphWin("Taion Tuesday", 500, 500)

  for i in range(10):
    sentence = (input("What would you like to say? "))
    point = win.getMouse()
    text = Text(point,sentence)
    text.draw(win)

def drawLineLoop():
    win = GraphWin("Line Input")

    for i in range(10):
        message = Text(Point(100, 100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")

def blueCircle():
    win = GraphWin("Blue Circle", 500, 500)
    center = win.getMouse()
    bCircle = Circle(center, 50)

    for i in range(50):
        win.getMouse()
        center = win.getMouse()
        bCircle = Circle(center, bCircle)
        bCircle.draw(win)
        bCircle.setFill("blue")


def drawRectangle():
    win = GraphWin("Rectangle", 200, 200)
    win.setCoords(0, 0, 200, 200)
    x = float(input("Give the width (less than 200) "))
    y = float(input("Give the length (less than 200) "))
    center = Point(100,100)

    rectangle = Rectangle(Point(50, 200-y), Point(200-x, 50))
    rectangle.draw(win)
    rectangle.setFill("black")

def drawArcheryTarget():
    win = GraphWin("Archery", 500, 500)
    center = Point(200, 200)
    myCircle = Circle(center, 160)
    myCircle.draw(win)
    myCircle.setFill("white")
    myCircle = Circle(center, 140)
    myCircle.draw(win)
    myCircle.setFill("black")
    myCircle = Circle(center, 100)
    myCircle.draw(win)
    myCircle.setFill("blue")
    myCircle = Circle(center, 60)
    myCircle.draw(win)
    myCircle.setFill("red")
    myCircle = Circle(center, 20)
    myCircle.draw(win)
    myCircle.setFill("yellow")


def drawCircle():
    win = GraphWin("Circle", 500, 500)
    center = Point(200, 200)
    r = int(input("What is the radius of the circle?"))
    myCircle = Circle(center, r)
    myCircle.draw(win)
    myCircle.setFill("red")
    win.getMouse()

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    rarm = Line(Point(100, 80), Point(50, 120))
    larm = Line(Point(100, 80), Point(150, 120))
    rleg = Line(Point(100, 120), Point(50, 220))
    lleg = Line(Point(100, 120), Point(150, 220))
    body.draw(win)
    rarm.draw(win)
    larm.draw(win)
    rleg.draw(win)
    lleg.draw(win)

def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")

blueCircle()
tenColouredRectangles()
tenStrings()
drawLineLoop()
drawRectangle()
drawArcheryTarget()
drawStickFigure()
drawLine()
drawCircle()
