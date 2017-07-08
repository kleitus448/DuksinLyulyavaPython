# -*- coding: Utf-8 -*-
from random import*
from string import*
def k(a,b):
	n = []
	for i in a:
		if i not in b:
			n.append(i)
	return n  
def gen_word():
	n = []
	alp = list((chr(x) for x in range(ord('A'),ord('Z')+1)))
	alp1 = ("A", "E", "I", "O", "U", "Y")
	alp2 = list(k(alp,alp1))
	g = randint(1,9)
	for i in range(g):
		if randint(0,3) in (0,1):
			n.append(choice(alp2))
		else:
			n.append(choice(alp1))
	n = tuple(n)
	n = "".join(n)
	return n
def gen_sent():
	n = []
	g = randint(1,15)
	for i in range(g):
		n.append(gen_word())
	n = tuple(n)	
	n = " ".join(n)	
	return n
def gen_some_sent():	
	n = []
	g = randint(1,15)
	for i in range(g):
		n.append(gen_sent())
	n = tuple(n)	
	n = ". ".join(n) + "."	
	return n
if __name__ == "__main__":
	print(gen_some_sent())
