# Данная программа работает только для положительных чисел, где a >= b
def sum(a, b):
    result = []  # результат операции

    # уравниваеем количество разрядов в числах
    if len(a) > len(b):
        b = [0] * (len(a) - len(b)) + b
    else:
        a = [0] * (len(b) - len(a)) + a
    n = len(a)

    temp = 0  # то, что нужно перенести в следующий разряд
    for i in range(n - 1, -1, -1):
        new_elem = (a[i] + b[i] + temp) % 1000
        result.append(new_elem)
        temp = new_elem // 1000

    # если что-то еще нужно перенести в новый разряд
    if temp != 0:
        result.append(temp)
    print_long_numbers(reversed(result))


def sub(a, b):
    result = []  # результат операции

    # уравниваеем количество разрядов в числах
    if len(a) > len(b):
        b = [0] * (len(a) - len(b)) + b
    else:
        a = [0] * (len(b) - len(a)) + a
    n = len(a)

    temp = 0
    for i in range(n - 1, -1, -1):
        new_elem = (a[i] - b[i] - temp)
        if new_elem < 0:
            new_elem = 1000 + new_elem
            temp = 1
        result.append(new_elem)

    # убираем лидирующие нули
    while result[-1] == 0 and len(result) >:
        result.pop()
    print_long_numbers(reversed(result))


# начальные данные
a = [1, 123, 123]
b = [1, 123, 123]

# сложение
print_long_numbers(a)
print(' + ', end='')
print_long_numbers(b)
print(' = ', end='')
sum(a, b)

print()

# вычитание
print_long_numbers(a)
print(' - ', end='')
print_long_numbers(b)
print(' = ', end='')
sub(a, b)