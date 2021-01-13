a = [randint(0, 100) for i in range(10)]
a.sort()

sum_first = 0
quantity_first = 0
sum_second = 0
quantity_second = 0
for elem in a:
    if elem < 50:
        sum_first += elem
        quantity_first += 1
    else:
        sum_second += elem
        quantity_second += 1
print(f'Среднее значение всех элементов <50: {sum_first/quantity_first}')
print(f'Среднее значение всех элементов >=50: {sum_second/quantity_second}')