import math

def main():
  #INPUT
  x = float(input("Please enter a number: "))
  #PROCESS
  y = 2*x + 2
  #OUTPUT
  print(y)

def squaring():
  z = float(input("Please enter z: "))
  v = float(input("Please enter v: "))

  z2 = z*z
  v2 = v*v
  p2 = z2+v2
  p = math.sqrt(p2)
  print(p)
  
#1)
def circumferenceOfCircle():
  radius = float(input("Please input the radius of a circle: "))
  circumference = 2*math.pi*radius
  print("The circumference is: ",circumference)
  
#2)
def areaOfCircle():
  radius = float(input("Please input the radius of a circle: "))
  area = math.pi*radius*radius
  print("The area of a circle is: ",area)

#3)
def costOfPizza():
  diameter = float(input("Please input the diameter of the pizza (in cm): "))
  rad = diameter/2
  pizzaArea = math.pi*rad*rad
  pizzaCost = math.sqrt(pizzaArea) * 1.50
  print("The pizza will cost: £",pizzaCost)

#4/5)
def slopeOfLine():
  x1 = float(input("Please enter x1: "))
  y1 = float(input("Please enter y1: "))
  x2 = float(input("Please enter x2: "))
  y2 = float(input("Please enter y2: "))
  
  slope = (y2-y1)/(x2-x1)
  distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

  print("The slope is: ",slope)
  print("The distance between points is: ",distance)

#6)
def travelStatistics():
  speed = float(input("Please enter your average speed by kilometers per hour: "))
  time = int(input("For how many hours were you driving? (whole hours): "))
  distance = speed*time
  print("You have travelled: ",distance," km" )
  litres = distance/5
  print("You have used", litres," litres of fuel")

#7)
def sumOfSquares():
  n = int(input("How many values are in the average?: "))
  sum = 0
  #Loop from 1 to n
  for num in range(1,n+1,1):
    sum = sum+num**2
  print("The sum of squares is:", sum)

#8)
def averageOfNumbers():
  n = int(input("How many values are in the average?: "))
  total = 0
  #Loop from 1 to n
  for i in range(n):
    number = int(input("Please enter term number of the sequence: "))
    total = total + number

  average = total/n
  print("Your average is:", average)
  
  
#Functions executed below
circumferenceOfCircle()
areaOfCircle()
costOfPizza()
slopeOfLine()
travelStatistics()
sumOfSquares()
averageOfNumbers()
#main()
#squaring()

