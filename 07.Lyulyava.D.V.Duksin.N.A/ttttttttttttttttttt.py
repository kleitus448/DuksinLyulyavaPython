from turtle import*

N = 100000000000

for i in range(N):
    fd(abs(i%40-20))
    left(5)


exitonclick()
