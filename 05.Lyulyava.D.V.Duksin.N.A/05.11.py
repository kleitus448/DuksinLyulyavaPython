s = []
y = eval(input())
for i in y :
    s += [i]
del s[s.index(max(s))]
print(max(s))
