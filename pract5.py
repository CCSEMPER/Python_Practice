# Practical Worksheet 5: Using functions
# Migle, up2112135


from graphics import *
import math



# For exercises 1 and 2
#radius param/circumference return
def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(radius):
    return math.pi * radius * 2

def circleInfo():
    radius = float(input("What is the radius of the circle?: "))
    print("The area is:",areaOfCircle(radius))
    print("The circumference is:",circumferenceOfCircle(radius))

# For exercise 3
centre = Point(250,250)
radius = 60
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


win = GraphWin("Brown Eye",500,500)
def drawBrownEyeInCentre():
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius / 2, "#964B00")
    drawCircle(win, centre, radius / 4, "black")

#4
width = 6
height = 3
def drawBlockOfStars(width,height):
    for x in range(height):
        print("*" * int(width))
    #Define width as an integer to multiply the *

def drawLetterE(width, height):
    drawBlockOfStars(width *2, height)
    drawBlockOfStars(width /2, height)
    drawBlockOfStars(width *2, height)
    drawBlockOfStars(width /2, height)
    drawBlockOfStars(width *2, height)
    #could loop this

# For exercise 5
centre = Point(190, 250)
radius = 60
def drawBrownEye(win, centre, radius):
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius / 2, "#964B00")
    drawCircle(win, centre, radius / 4, "black")

    win.getMouse()

def drawPairOfBrownEyes():
    for i in range(2):
        x = 250*1 +60
        y = 250
        centre = Point(x,y)
        drawBrownEye(win, centre, radius)
        win.getMouse()

p1 = win.getMouse()
p2 = win.getMouse()
#6 can add prompt to click 2 points
def distanceBetweenPoints(p1, p2):
    p1x = p1.getX()
    p1y = p1.getY()
    p2x = p2.getX()
    p2y = p2.getY()

    dist = math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)
    print(dist)

#7
def drawBlocks(spaces1, stars1, spaces2, stars2, height):
    for i in range(height):
        print(f"{' ' * spaces1}{'*' * stars1}{' ' * spaces2}{'*' * stars2}")


def drawLetterA():
    drawBlocks(1,4,0,4,2)
    drawBlocks(0,2,6,2,2)
    drawBlocks(0,5,0,5,2)
    drawBlocks(0,2,6,2,3)

def main():
    drawLetterA()
    circleInfo()
    drawBrownEyeInCentre()
    drawLetterE(width,height)
    drawPairOfBrownEyes()
    distanceBetweenPoints(p1, p2)
main()

