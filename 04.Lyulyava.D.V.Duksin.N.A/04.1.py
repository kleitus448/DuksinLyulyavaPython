from math import *

x = float(input("Введите x: "));
y = float(input("Введите y: "));
z = float(input("Введите z: "));

a = (1+y)*(x+(y/(pow(x,2)+4)))/(exp(-x-2)+pow(pow(x,2)+4, -1));
b = (1 + cos(y-2))/(pow(x,4)/2+pow(sin(z),2))
print("a =", a, "b =", b);

