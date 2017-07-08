a = int(input());
b = int(input());
c = int(input());
print("Наибольшее число при расчёте по 1 варианту: ", end = '');
if (a > b) and (a > c) : print(a); 
elif (b > a) and (b > c) : print(b);
elif (c > a) and (c > b): print(c);
else : print ("Нет наибольшего");

print("Наибольшее число при расчёте по 2 варианту: ", end = '');
print(a if (a > b) and (a > c) else 
      b if (b > a) and (b > c) else 
      c if (c > a) and (c > b) else ("Нет наибольшего"));

 
