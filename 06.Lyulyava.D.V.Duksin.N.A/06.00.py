def rasst(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

print(rasst((0,0),(10,10)))
