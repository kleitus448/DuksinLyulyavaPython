from math import *
print("ax^2 + bx + c = 0");
a = int(input("Введите a: "));
while a == 0 :
    print("a меньше нуля");
    a = int(input("Введите a снова: "));
b = int(input("Введите b: "));
c = int(input("Введите c: "));
Diskr = pow(b,2) - 4*a*c;
if Diskr < 0 : print("Дискриминант отрицательный, действительных решений нет")
else:
    x1 = (-b + pow(Diskr, 1/2))/(2*a)
    x2 = (-b - pow(Diskr, 1/2))/(2*a)
    print ("x1 = ", x1, "x2 = ", x2)
