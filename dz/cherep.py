import turtle

def drawHouse(t, length):
	t.color("brown")
	t.begin_fill()
	for i in range(4):
		t.forward(length)
		t.right(90)
	t.end_fill()
	t.color("black")
	t.begin_fill()
	t.left(45)
	t.forward(length/(2)**(1/2))
	t.right(90)
	t.forward(length/(2)**(1/2))
	t.right(135)
	t.end_fill()
	t.forward(length)

window = turtle.Screen()
pencil = turtle.Turtle()
drawHouse(pencil,150)
window.exitonclick()
