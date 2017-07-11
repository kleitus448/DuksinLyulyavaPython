#Пушкин Антон

#enter whole numbers until 0, and record only positive ones in the file

f = open('data','wt')
n=int(input())
while n:
    if (n>0):
        print(n,file=f)
    n=int(input)
f.close()
