zap = eval(input())
print(zap)
Count = 0
line  = input()
for u in range(len(zap)):
    if zap[u].find(line):        
        line = line.replace(zap[u],"")              
print(line)

