# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# 6782 -> 23
# 0,56 -> 11

number = input('Введие число: ')

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def float_to_int(x):
    if isfloat(x) == True:
        x.replace(".", "")
    return x

def summa_with_int(number):
    result_sum = 0
    while number != 0:
        result_sum += number % 10
        number //= 10
    print(result_sum)

def float_sum(num):
    x = num.split(".") 
    a = int(x[0])
    b = int(x[1])
    summa = 0
    while (a != 0):
        summa = summa + (a % 10)
        a = a // 10
    while (b != 0):
        summa = summa + (b % 10)
        b = b // 10
    print("Сумма цифр равна:", summa)

if isint(number) == False and isfloat(number) == False:
    print('Вы ввели не число.')
elif isint(number) == True:
    summa_with_int(int(number))
elif isfloat(number) == True:
    float_sum(str(number))