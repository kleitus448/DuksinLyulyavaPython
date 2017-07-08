'''Модуль генерации шуток про украину'''
def GabenSaloUkraine:
'''Генератор случайных ПРОИЗНОСИМЫХ слов
          Copyleft by Nikita Duksin'''
    from random import *
    alp1 = ["А","О","У","Ы","Э","Я","Ё","Ю","И","Е"]
    alp2 = ["Б","В","Г","Д","Ж","З","К","Л","М","Н","П","Р","С","Т","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ь"]
    for i in range(10):
        Slovo = []
        for j in range(randint(1,9));
            Slovo.append(choice(alp2))
            Slovo.append(choice(alp1))
        print("".join(Slovo))    

print("Слава украине, пользуйся наздоровье!")
