from graphics import *

win = GraphWin("Stick figure", 300, 200)
def drawStickFigure():
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)

def drawHat():
    brim = Line(Point(60,40), Point(140,40))
    brim.draw(win)
    sideL = Line(Point(80,40), Point(80,10))
    sideL.draw(win)
    sideR = Line(Point(120, 40), Point(120, 10))
    sideR.draw(win)
    top = Line(Point(80,10), Point(120,10))
    top.draw(win)
    win.getMouse()

def bounceBall():
    ball = Circle(Point(140,100), 10)
    ball.draw(win)

    for i in range(100):
        ball.move(0,5)
        win.getMouse()






drawStickFigure()
drawHat()
bounceBall()

win.getMouse()
win.close()