#! python
import random
def matri(): 
	a = []
	g = random.randint(1,20)
	h = random.randint(1,20)
	for i in range(g):
		a.append([random.randint(0,9) for _ in range(h)])	
	return a,g,h	

if __name__ == "__main__":
	a,g,h = matri()
	for i in range(g):
		for u in range(h):
			print a[i][u],	
		print 
