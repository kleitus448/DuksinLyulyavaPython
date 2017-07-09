from math import *
c = input("Выберите вариант (а, б, в, г): ");
res = 0;
while c not in ['а', 'б', 'в', 'г'] :
    print("Поробуйте ещё раз");
    c = input("Выберите вариант (а, б, в, г): ");
a = int(input("Введите a: "));
if c == 'а' :
    if (-2 <= a < 2) :
        res = a*a
    else : 
        res = 4
elif c == 'б' :
    if a <= 2 :
        res = a*a + 4*a + 5 
    else : 
        res = 1/(a*a + 4*a + 5)
elif c == 'в' : 
    if a <= 0 :
        res = 0  
    elif 0 < a <= 1 : 
        res = a 
    else :
        res = pow(a, 4)
elif c == 'г' :
    if a <= 0 : 
        res = 0 
    elif 0 < a <= 1 :
        res = a*(a-1) 
    else :
        res = a*a - sin(pi*x*x)
print(res);
