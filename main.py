"""
HW-09 Solution
"""

import turtle

# Global variables and objects
sideOfSquare = 50
casper = turtle.Turtle()

# Function definitions
def square(turtleName, x,y):
  turtleName.penup()
  turtleName.goto(x,y)
  turtleName.pendown()
  for i in range(4):
    turtleName.forward(sideOfSquare)
    turtleName.left(90)

# Instructions for user
print ("Enter (x,y) coordinates to draw a square with a length of " + str(sideOfSquare) +"pixels")
print ("(x,y) specifiy the bottom left corner of the square")
print ("Your x and y coordinates should be between -150 and 150 pixels from the origin.")

# Ask for user input
xPositionStr = input("Enter the x coordinate for the bottom left vertex:")
yPositionStr = input("Enter the y coordinate for the bottom left vertex:")

xPosInt = int(xPositionStr)
yPosInt = int(yPositionStr)

if (xPosInt<-150) or (xPosInt>150) or (yPosInt<-150) or (yPosInt>150):
  print("One of your coordinates is out of bounds, not drawing anything...")
else:
  print("Drawing a square at x = " + str(xPositionStr) + " and y = " + str(yPositionStr))
  square(casper,xPosInt,yPosInt)





