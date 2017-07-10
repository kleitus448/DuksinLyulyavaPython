from без1имени import*
some_Sent = gen_some_sent()
word = input("Введите слово для подсчёта: ")
while word:
	print("Слово", word, "встречается", some_Sent.count(word), "раз")
	word = input("Введите слово для подсчёта: ")
