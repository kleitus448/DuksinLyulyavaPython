import turtle
import random
def drawTree(t,n,k,l,s,h):
	'''Print 1 tree'''
	m = ((k-l)/n)
	for i in range(1,n+1):
		t.down()
		t.color("green")
		t.begin_fill()
		for j in range(3):			
			t.forward(k)
			t.left(120)
		t.end_fill()
		t.up()
		t.setheading(90)
		t.forward(k*(3**(1/2))/2)
		t.setheading(0)
		t.forward(m/2)
		k = k-m
	t.home()
	t.setx(h+10*(s+1))
def drawForest(n):
	'''Print forest consist of trees'''
	window = turtle.Screen()
	pencil = turtle.Turtle()
	h = 0
	for i in range(n):
		n,k,l = random.randint(1,9),random.randint(50,90),random.randint(20,60)
		h += k
		drawTree(pencil,n,k,l,i,h)

	window.exitonclick()
if __name__ == "__main__":
	drawForest(int(input("Введите число деревьев в лесу: ")))
