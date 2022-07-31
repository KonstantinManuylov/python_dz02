# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from datetime import datetime

numbers_amount = int(input('Сколько чисел необходимо? '))
numbers_list = []
i = 1
random_number = datetime.now()

while i <= numbers_amount:
    # print(((int(random_number.strftime("%f"))) * i) ** 2 % 100)
    numbers_list.append(((int(random_number.strftime("%f"))) * i) ** 2 % 100)
    i += 1

print(numbers_list)

"""
Мне не нравится это решение, но в данный момент я не могу придумать ничего лучше.
"""