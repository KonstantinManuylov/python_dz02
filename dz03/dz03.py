# Задайте словарь из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

base_number = input('Введите число: ')
numbers_dictionary = {}
i = 1
values_sum = 0


def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


if isint(base_number) == False:
    print('Введенное значение не является числом.')
else:
    while i <= int(base_number):
        numbers_dictionary[i] = (1 + 1 / i) ** i
        values_sum += numbers_dictionary[i]
        i += 1
    print(numbers_dictionary)
    print(f'Сумма значений {round(values_sum, 3)}')
