s = eval(input())
print([s[i] for i in range(len(s)) if i%2==1])
print([s[len(s)-i-1] for i in range(len(s)) if i%2==0])
