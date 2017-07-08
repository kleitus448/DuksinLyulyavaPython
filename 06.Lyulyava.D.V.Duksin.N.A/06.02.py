def Sum(*l) :
    s = l[0]
    for c in l[1:]:
        s += c
    return s
    
print(Sum(2,3,4,5,6))    

