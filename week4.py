

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

    if marks in range (8,10):
        x = 0
    elif marks in range (7,6):
        x = 1
    elif marks in range (5,4):
        x = 2
    else:
        x = 3

    print("The grade you received was:",grades[x])
    #fix else statement





gradeTest()
generateEmail()
personalGreeting()
formalName()
kilos2pounds2()

