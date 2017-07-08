from random import *
N = 1000
y, n = 0, 0
for i in range(N):
    i = randrange(3);
    if i in [0,1]: 
        print("No");
        n += 1
    else: 
        print("Yes");
        y += 1
print("На",N, ":", y,"YES,",n,"NO!")
    
