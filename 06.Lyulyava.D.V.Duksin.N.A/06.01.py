def ded32(s, n, m):
    return (s[:n]+s[-m:])
    
s, n, m = eval(input())
print(ded32(s,n,m))
