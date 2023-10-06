from graphics import *

def drawStickFigure():
    pass
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 100))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 100))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)

def animatedBall():
    win = GraphWin("Animation",500,500)
    p = win.getMouse()

    c = Circle(p,10)
    c.setFill("pink")
    c.setOutline("pink")
    c.draw(win)

    for i in range(100):
        c.move(1,0)






animatedBall()