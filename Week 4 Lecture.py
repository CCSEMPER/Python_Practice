from graphics import *

def main():
  secretWord = "OscarWilde"
  character = int(input("Which character do you want? "))
#strings treat each character like an index. the first character is 0.
  index = character - 1 #starts at 1 instead of 0
  print(secretWord[index])
  

def main2():
  word = "HarlanEllison"
#loops and prints every letter in "word"
  for letter in word: #Best for strings
    print(letter)

  #length = len(word) #Better for integers
  #for i in range(length):
  #  print(word[i])

def main3():
  pi = 3.14159254
  pi2 = 3.6756756757567
  print("PI is {:0.2f}".format(pi)) #.2f = 2d.p
  print("My values are {1:0.3f} and {0:.2f}".format(pi,pi2)) #index:int.decimalfloat

def main4():
  win = GraphWin("", 500, 500)
  sentence = "can you see what is going on?"
  size = len(sentence)
  offset = 10

  for i in range(size):
    point = win.getMouse()
    text = Text(point,sentence[i])
    text.draw(win)




  #repeating pattern ver
    #x = i*15
    #y = i*15
    #point = Point(x,y)
    #text = Text(point,sentence)
    #text.draw(win)

main4()
main3()
main2()
main()