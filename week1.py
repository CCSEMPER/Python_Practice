#Creating and overwriting a variable
x = 7 #a constant, cannot change unless affected by console
y = x+1

#1)
def sayName():
  name = "Migle Vaivadaite"
  print(name)

#2)
def sayHello2():
  print("Hello")
  print("World")
#Alternatively
  print('''Hello
  World''')

#3)
def euros2pounds():
  euro = int(input("Welcome to EUR to GBP converter. Please state the amount of EUR you'd like to convert: "))
  print("That's", euro/1.17 ,"Pounds")

#4)
def sumDiff():
  num1 = int(input("Please input your first number: "))
  num2 = int(input("Please input your second number: "))
  sum = num1 + num2
  difference = num1 - num2
  print("The sum of these numbers are: ",sum)
  print("The difference of these numbers are: ",difference)

#5)
def changeCounter():
  onePence = int(input("How many 1p coins do you have? "))
  twoPence = int(input("How many 2p coins do you have? "))
  twoPence = twoPence *2
  fivePence = int(input("How many 5p coins do you have? "))
  fivePence = fivePence *5
  totalPence = onePence+twoPence+fivePence
  print("You have ",totalPence,"p")

#6)
def tenHellos():
  for i in range(10):
    print("Hello World!")

#7)
def countTo():
  number = int(input("Pick a number to count to: "))
  for i in range(1,number+1):
    print(i)

#8)
def zoomZoom():
  zoomNum = int(input("Pick a number: "))
  for i in range(1,zoomNum+1):
    print("zoom",i)

#9)
#def weightsTable():
sayName()
sayHello2()
euros2pounds()
sumDiff()
changeCounter()
tenHellos()
countTo()
zoomZoom()