from igra_s_bukv import*
Count = 0
i = input("Vvedite slovo(stroku): " )
i.decode('utf-8')
g = gen_some_sent()
for t in range(len(g)):
	if i in g:
		Count+=1
print(Count)
