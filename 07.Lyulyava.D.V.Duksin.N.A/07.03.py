N = int(input())
sp = []
for i in range(N):
    sp.append(input())
for i in zip(*sp):
    print(*i);
   
