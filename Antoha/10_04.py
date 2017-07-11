#Пушкин Антон

#two words are entered (with a space)
#outputs a word that contains the letters in the first one,
#but not in the second

a,b=input().split()
print(''.join(set(a)-set(b)))
