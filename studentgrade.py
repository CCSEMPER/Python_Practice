class Student:
    def __init__(self, upNumber):
        self.up = upNumber
        self.graduated = False
        self.credits = 0

    def getCredits(self):
        return self.credits

    def graduate(self):
        self.graduated = True

    def addCredits(self, creditsRewarded):
        self.credits = self.credits + creditsRewarded

    def __str__(self):
        msg = "Student with UP number {}, ".format(self.up)
        msg = msg + "has {} credits, ".format(self.credits)
        if self.graduated:
            msg = msg + "and has graduated."
        else:
            msg = msg + "and has not graduated yet."
        return msg


class Course:
    def __init__(self, name):
        self.students = []
        self.name = name

    def addStudent(self, student):
        self.students.append(student)

    def getStudents(self):
        return self.students

    def getAverageCredits(self):
        total = 0
        for student in self.students:
            total = total + student.getCredits()
        return total / len(self.students)

    def graduateStudent(self, index):
        self.students[index].graduate()

    def addCreditsToStudent(self, index, credits):
        self.students[index].addCredits(credits)

    def __str__(self):
        msg = "Course {} has the following students:\n".format(self.name)
        for student in self.students:
            msg = msg + "{}\n".format(student)
        return msg


def testCourse():
    compSci = Course("Computer Science")
    compSci.addStudent(Student(123456))
    compSci.addStudent(Student(234567))
    print("Average credits is", compSci.getAverageCredits())
    compSci.graduateStudent(0)
    print("Average credits is", compSci.getAverageCredits())
    compSci.addCreditsToStudent(1, 10)
    print("Average credits is", compSci.getAverageCredits())
    print(compSci)

testCourse()