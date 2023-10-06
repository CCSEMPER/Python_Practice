import os
from graphics import *


#1
def personalGreeting():
    name = str(input("What is your name? "))
    print("Hello "+ name + ", nice to see you!")

#2
def formalName():
    fName = str(input("What is your first name? "))
    lName = str(input("What is your last name? "))
    fInitial = fName[0]
    print("Your formal name is "+ fInitial+". "+lName)

#3
def kilos2pounds2():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The {0:0.2f} kilos in pounds is {1:0.2f}".format(kilos, pounds))
    #fix so that the 2dp doesn't round up??

#4
def generateEmail():
    firstName = str(input("What is your first name? "))
    lastName = str(input("What is your last name? "))
    entryDate = int(input('What year did you join the university? '))

    #lastName = lastName.lower
    #firstName = firstName.lower

    int(entryDate)
    dateShort = entryDate % 100
    dateShort = str(dateShort)
    email = ("Your email is: "+lastName[0:4]+"."+firstName[0]+"."+dateShort+".@myport.ac.uk")
    print(email.lower())
    #format into all lowercase

def gradeTest():
    marks = int(input("How many marks do you have? "))
    grades = "ABCF"
    int(marks)

    if 7 < marks <= 10:
        print("The grade you received was:", grades[0])
    elif 5 < marks <= 7:
        print("The grade you received was:", grades[1])
    elif 3 < marks <= 5:
        print("The grade you received was:", grades[2])
    elif -1 < marks <= 3:
        print("The grade you received was:", grades[3])
    else:
        print("invalid value")

def graphicLetters():
    pass
    win = GraphWin("Taion Tuesday", 500, 500)
    sentence = (input("Type a word: "))

    size = len(sentence)
    offset = 10

    for i in range(size):
        point = win.getMouse()
        text = Text(point, sentence[i])
        text.setSize(20)
        text.draw(win)

def singASong():
    word = (input("Type a word: "))
    lines = int(input("How many lines: "))
    length = int(input("How long each line is: "))
    word = word + ' '
    for i in range(lines):
        print((word * length))


def makeInitialism():
    words = input("Please make a sentence: ")
    splitwords = words.split()
    initials = ""
    for i in range(len(splitwords)):
        initials = initials + (splitwords[i][0])
    print(initials)

def fileInCaps():
    contents = inFile.read()
    contents = contents.upper
    print(contents)
    inFile.close()


singASong()
makeInitialism()
#graphicLetters()
gradeTest()
generateEmail()
personalGreeting()
formalName()
kilos2pounds2()

