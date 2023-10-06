# Practical Worksheet 6: if statements and for loops
# your name, your number


from graphics import *
import math

#1
def fastFoodOrderPrice():
    foodCost = float(input("What is the total of the order? "))

    if foodCost >= 10:
        delivery = 0
    elif foodCost < 10:
        delivery = 1.50
    else:
        pass
    totalOrder = foodCost + delivery
    print("Your total cost with delivery is: £",totalOrder)

#2
def whatToDoToday():
    temperature = float(input("What's the temperature outside? "))

    if temperature > 25:
        print("You should swim in the sea today.")
    elif temperature <= 25 and temperature >= 10:
        print("You should shop at Gunwharf Quays today.")
    elif temperature < 10:
        print("You should watch a movie at home.")
    else:
        pass

#3
start = int(input("Give the first number to square root: "))
end = int(input("Give the last number to square root: "))
def displaySquareRoots(start,end):

    for i in range(start,end+1):
        print("The square root of",i,"is",format(math.sqrt(i), '.3f'))

#4
marks = int(input("How many marks do you have? "))
grade = ""
def gradeTest(marks):

    global grade

    if marks <= 20 and marks >= 16:
        grade = "A"
    elif marks < 16 and marks >= 12:
        grade = "B"
    elif marks < 12 and marks >= 8:
        grade = "C"
    elif marks < 8 and marks >= 0:
        grade = "F"
    else:
        grade = "X"

    return grade


#5
#all variables needed
number = int(input("How many peas are there? "))
radius = 50
length = number * 100
height = number * 20
win = GraphWin("Peas",length,height)
i = number



def peas(win,centre,radius): #pass info needed into parenthesis
  c = Circle(centre,radius)
  c.setFill("green")
  c.draw(win)


def peasInAPod():
    for x in range(0, 500,50):
        x = x + 100
        y = 50
        centre = Point(x, y)
        peas(win,centre,radius)
        win.getMouse()






# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8
def drawColouredEye(win, centre, radius, colour):
    pass
    # remove the pass and add your code here

#9
def line(win, p1, p2, colour):
    l = Line(p1,p2 )
    l.setOutline(colour)
    l.draw(win)
    return l

def line2(win, p3, p4, colour):
    l2 = Line(p3,p4 )
    l2.setOutline(colour)
    l2.draw(win)
    return l2

def text(win, point, text,colour):
    t = Text(point,text)
    t.setOutline(colour)
    t.draw(win)
    return t

def drawPatch():
    win = GraphWin("Patch",100,100)
    x = Point(25,0)
    y = Point(25,100)
    colour = "red"

#vertical lines
    for y in range(0,100,25):
        for x in range(13,100,25):
            p1 = Point(x,y)
            p2 = Point(p1.x, 100)
            line(win, p1, p2, colour)
            win.getMouse()


    i = Point(0,25)
    j = Point(0,100)

#horizontal lines
    for j in range(0,100,25):
        for i in range(13,100,25):
            p3 = Point(i,j)
            p4 = Point(p3.x, 100)
            line2(win, p3, p4, colour)











def countdown():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")

#countdown()
#fastFoodOrderPrice()
#whatToDoToday()
#displaySquareRoots(start,end)

#gradeTest(marks)
print("The grade you received was:", grade)
drawPatch()
#peasInAPod()
