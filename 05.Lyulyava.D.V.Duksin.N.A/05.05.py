print([i%3 for i in range(10,40,2)])
print([(i,i**2,i**3) for i in range(10,40)])
print([(x,i) for i,x in enumerate(range(1,40,2)) if x!=13 and i != 13])
