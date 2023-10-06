from graphics import *

#function library
def line():
  pass

def myCircle(win,centre,radius,colour): #pass info needed into parenthesis
  c = Circle(centre,radius)
  c.setFill(colour)
  c.draw(win)

def rectangle():
  pass

#Entry Point
def main():
  print("# Lectures live coding #")
  size = 700
  win = GraphWin(" # Lectures live coding #", size, size)

  radius = 50
  colours = ["Blue","Orange","Red"]

  for i in range(3):
    x = 100*i + 100
    y = 100
    centre = Point(x,y)
    colour = colours[i]
    myCircle(win,centre,radius,colour)

  win.getMouse()
#to make circles move vertically, swap x and y values
#win.getMouse() forces window to stay on screen


#Exec entry point
main()
