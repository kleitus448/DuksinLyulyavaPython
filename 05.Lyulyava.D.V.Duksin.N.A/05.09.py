N =  int(input("Введите количество строк "))
c = []
for e in range(N):
    c=c+[input("Введите строку ")]
print([c[i] for i in range(N) if i%2==0])
    
