N,M = eval(input())

Matrix = []
for i in range(N):
    Matrix.append(eval(input()))
    
'''import pprint
pprint.pprint(Matrix)'''
for col in zip(*Matrix):
    print(*col)
