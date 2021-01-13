from random import randint
a = [randint(20, 100) for i in range(10)]
even = sum([elem for elem in a if elem %2 == 0])
odd = sum(a) - even
print(f'Сумма нечетных элементов = {even}; сумма четных элементов = {odd}')