from graphics import *

radius = 50
centre = Point(50, 50)
def circle(win,centre,radius,colour):
    c = Circle(centre,radius)
    c.setFill(colour)
    c.draw(win)
    return c



def main():
    win = GraphWin("Circles", 400, 400)
    win.getMouse()
    colour = ["Blue","Cyan","Purple","Magenta"]

    for y in range (50, 400, 100):
        for x in range (0, 400,100):
            point = win.getMouse()
            x = x + 50
            y = y
            centre = Point(x, y)
            if (point.getX() < 200 and point.getY() < 200):
                circle(win, centre, radius, colour[0])
            elif (point.getX() >= 200 and point.getY() < 200):
                circle(win, centre, radius, colour[1])
            elif (point.getX() < 200 and point.getY() >= 200):
                circle(win, centre, radius, colour[2])
            elif (point.getX() >= 200 and point.getY() >= 200):
                circle(win, centre, radius, colour[3])
            else:
                pass
            win.getMouse()

main()