
from turtle import *
penup()
goto(-100,-100)
pendown()
def koch(delka, level):
    if level > 0:
        for t in [60, -120, 60, 0]:
            
            koch(delka, level -1)
            left(t)
    else:
        forward(delka)

speed(0)
koch(30, 9)

exitonclick()