def summ(a):
    '''Summa cifr chisla'''  
    summa = 0
    for i in a:
        summa += int(i)
    return summa  

def minimum(s):
    '''poisk chisel s min sum cifr'''
    s1 = []
    e = []
    for i in s :
        s1 += [summ(i)]
    u = s1.count(min(s1))    
    for t in range(u): 
        e += [s1.index(min(s1))+t]
        del s1[s1.index(min(s1))] 
    s1.clear()      
    for m in range(len(e)):        
        s1 += [s[e[m]]]
    return s1
