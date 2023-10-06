# Practical Worksheet P3: Graphical Programming
# your name, your number

from graphics import *


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

drawStickFigure()
drawLine()