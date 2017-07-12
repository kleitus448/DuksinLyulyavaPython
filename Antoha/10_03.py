#Пушкин Антон

# testing hash() function

import random
from math import*

def testhash(f,seq,n):
    '''apply a number hash() function to all the elements 
    in a sequence, then calculate and return the list, how many times 
    f(e) == 1,2,...,n, where 0...n - 03 f()'''
    gist=[0]*n
    for e in seq:
        gist[f(e)]+=1
    return gist

def hash1(a):
    return a%10
    
def hash2(a):
    return int(sin(a)*1000)%10

def hash3(a):
    return (a^random.randrange(100))%10

    
SEQSZ=10000

random.seed=100500
seq=(random.randrange(10,100,11) for i in range(SEQSZ))
gist=(testhash(hash3, seq, 10))
print(gist,(max(gist)-min(gist))*100/SEQSZ)
