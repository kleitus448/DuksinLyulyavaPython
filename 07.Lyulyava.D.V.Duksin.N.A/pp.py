import sys

print("###", sys.argv,"###")
if len(sys.argv)>1:
    NUM = int(sys.argv[1])
else:
    NUM = 4
    
for i in range(NUM):
    print("qq")        
