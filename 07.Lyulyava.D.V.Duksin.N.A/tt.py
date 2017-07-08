import random

MAXSEQ = 10000
COUNTERS = 10

counter = [0]*COUNTERS

for i in range(MAXSEQ):
    r = random.random()  
    counter[int(r*COUNTERS)] += 1
print(counter)    
print((max(counter)-min(counter))*100/MAXSEQ)
