b = input()
type(b)
print(max(tuple(b)))
l=b.count(max(tuple(b)))
print(l)
for y in range(l):		
		del b[b.index(max(b))]
print([max(b) if b == 0 else "None"])

