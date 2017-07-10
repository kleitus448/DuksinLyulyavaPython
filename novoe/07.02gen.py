import random
M, N = random.randint(3,12), random.randint(3,12)
print("{},{}".format(N,M))
for i in range (N):
    for j in range(M):
        cell = random.randrange(10,99)
        print(cell, end =  ",")
        print(cell, end = ",", file=sys.stderr)
    
    print()
    print(file=sys.stderr)
    print("="*60, file=sys.stderr)
