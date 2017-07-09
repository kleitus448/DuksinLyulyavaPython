i = 0;
a = int(input("Введите первый член последовательности: "));
Sum = 0;
while (a != 0) :
    i += 1;
    a = int(input("Введите next член: "));
    Sum += a;
if Sum : print("Cреднее арифметическое: ", Sum/(i-1)); 
