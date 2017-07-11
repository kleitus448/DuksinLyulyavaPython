from turtle import*
from math import* 

setup(1400,800)
i=-4
pensize(5)
speed(0)
penup()
while i<=5:
    setpos(i*100,sin(5*i)*100)
    pendown()
    i+=0.01

exitonclick()
