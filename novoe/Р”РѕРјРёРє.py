from turtle import*
from math import*

def drawHouse(t,length):
	for i in range(4):
		t.forward(length)
		t.right(90)
	t.left(45)
	t.forward(length/math.sqrt(2))
	t.right(90)
	t.forward(length/math.sqrt(2))	
	t.right(135)
	t.forward(length)

window = turtle.Screen()
pencil = turtle.Turtle()
pencil.pensize(2)
drawHouse(pencil,150)
window.exitonclick()	
