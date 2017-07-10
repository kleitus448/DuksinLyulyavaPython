for a in range(1,10):
    for b in range(a,10):
        for c in range(b,10):
            if ((a+b>c) and (a+c>b) and (b+c>a)):
                p = (a+b+c)/2
                s = (p*(p-a)*(p-b)*(p-c))**0.5
                print([a,b,c,s])    
