def stone_sort(a, condition=lambda a, b: a > b):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if condition(a[i], a[j]):
                a[i], a[j] = a[j], a[i]
    return a


print('Введите массив:')
a = list(map(int, input().split()))
print('Введите число:')
x = int(input())

a = stone_sort(a, lambda a, b: a < b)
print(f'Отсортированный массив: {a}')
counter = 0
for index, elem in enumerate(a):
    if elem == x:
        print(f'a[{index}] == {x}')
        counter += 1
    elif elem < x:
        break
print(f'Элементов в массиве, равных {x}: {counter}')
