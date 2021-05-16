# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

import turtle
t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(4)
turtle.speed(0)

while(True):
    for i in range(6):
      for colors in["orange","violet","green","yellow","red"]:

            turtle.color(colors)
            turtle.circle(100)
            turtle.left(100)

turtle.hideturtle()
turtle.mainloop()

