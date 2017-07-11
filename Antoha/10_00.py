#Пушкин Антон

#enter the strings until the empty one, out put the
#one with the biggest number of 'k' symbols


l=[]
s=input()
l+=[s]
while s:
    s=input()
    l+=[s]

print(len(max(l, key=lambda s: s.count('F'))))

print(max(((s.count('F'),len(s)) for s in l))[1])
