#Пушкин Антон

#enter text from the file 
#show the most popular word with the length bigger than 3

f=open('anna.txt','r')

s=f.read().lower()
dic={}
s=s.split()
for i in s:
    if len(i)>3:
        dic[i]=dic.get(i,0)+1 
        
ii=max(dic.values())        
print(ii)

for e in dic:
    if dic[e] == ii:
        print(e,ii)
        break

#s=''.join(c if c.isalpha() else ' ' for c in f.read())
