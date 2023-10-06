from graphics import *

win = GraphWin("Teacher", 300, 200)

def teacher():
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 80))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 80))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)
    win.getMouse()

def marker():
    rectangle = Rectangle(Point(165, 70), Point(180, 96))
    rectangle.draw(win)
    rectangle.setFill("brown")
    win.getMouse()

    rectangle2 = Rectangle(Point(170, 62), Point(175, 70))
    rectangle2.draw(win)
    rectangle2.setFill("brown")
    win.getMouse()

def whiteboard():
    rectangle3 = Rectangle(Point(25, 25), Point(125, 125))
    rectangle3.draw(win)
    rectangle3.setFill("white")
    win.getMouse()

def letters():
  words = ("ABCDEF")
  #words.setsize(36)
  #splitwords = words.split()

  #initials = ""
  for i in range(len(words)):
    point = Point(75, 75)
    text = Text(point, words[i][0])
    text.draw(win)
    win.getMouse()
    text.undraw()
    win.getMouse()




teacher()
marker()
whiteboard()
letters()
