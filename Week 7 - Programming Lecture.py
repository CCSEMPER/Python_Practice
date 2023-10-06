from graphics import *

# FUNCTIONS


def myCircle(win,centre,radius,colour):
    c = Circle(centre,radius)
    c.setFill(colour)
    c.draw(win)


def myRect(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint,brPoint)
    r.setFill(colour)
    r.draw(win)

def myLine(win, tlPoint, brPoint, colour):
    line = Line(tlPoint, brPoint)
    line.setFill(colour)
    line.draw(win)

def myText(win, point, text):
    pass

def myPolygon(win,listOfPoints,colour):
    pass


def print10():
    print("-" * 10)


def menu():
    print10()
    print("-- MENU --")
    print10()
    print("Select an option")
    print("1 - circle")
    print("2 - rect")
    print("3 -")
    print10()
    return int(input("please select an option: "))


# ENTRY POINT
def main():
    win = GraphWin("", 500, 500) #win takes priority in hierarchy

    selection = menu()
    if selection == 1:
        centre = Point(250,250)
        radius = int(input("Please input the radius: "))
        colour = "Blue"

        myCircle(win, centre, radius, colour)
        win.getMouse()

    elif selection == 2:
        tlPoint = win.getMouse()
        brPoint = win.getMouse()
        colour = "Blue"

        myRect(win, tlPoint, brPoint, colour)
        win.getMouse()

    elif selection == 3:
        win = GraphWin("Line", 500, 500)
        tlPoint = win.getMouse()
        brPoint = win.getMouse()
        colour = "Blue"

        myLine(win, tlPoint, brPoint, colour)
        win.getMouse()
    else:
        pass

# EXEC (ENTRY POINT)
main()