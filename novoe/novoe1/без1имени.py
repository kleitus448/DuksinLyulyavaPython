from random import*
from string import*
def gen_word():
	n = ""	
	alp1 = "ауоыиэяюёе"
	alp2 = "бвгджзйклмнпрстфхцчшщ"	
	g = randint(1,9)
	for i in range(g):
		if randint(0,3) in (0,1):
			n += (choice(alp2))
		else:
			n += (choice(alp1))	
	return n
def gen_sent():
	n = ""
	g = randint(1,15)
	for i in range(g):
		n += gen_word()	+ " "			
	return n
def gen_some_sent():	
	n = ""
	g = randint(1,15)
	for i in range(g):
		n += gen_sent() + "\n"
					
	return n
if __name__ == "__main__":
	print(gen_some_sent())
  
