# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = input('Введите число: ')
multi = 1
i = 1

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

if isint(number) == False:
    print('Вы ввели не число')
else:
    while i <= int(number):
        multi *= i
        print(multi)
        i += 1