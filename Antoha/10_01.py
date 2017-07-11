#Пушкин Антон

#generates strings for 10.00py
#strings are added one after another from the letters a-z,
#then in a random position letters 'F' are inserted  

from random import*

alp = ''.join(chr(i) for i in range(ord('a'),ord('z')+1))
MAXSTR=20
MAXLEN=32
MAXF=10

for i in range(randint(1,MAXSTR)):
    seq=(''.join(choice(alp) for j in range(randint(1,MAXLEN))))
    print(''.join(seq), end='')
    print('F'*randint(1,MAXF),end='f')
    seq=(''.join(choice(alp) for j in range(randint(1,MAXLEN))))
    print(''.join(seq))
print()
    

# rand_str():
#    alp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#    n=randint(0,5)
#   l=[]
#    for i in range(n):
#        nn=randint(0,10)
#        l+=[join(sample(alp,nn))]
#    print(l)
#        
#rand_str()
        
