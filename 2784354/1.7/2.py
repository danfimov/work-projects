a = list(map(int, input().split()))
max_count = 1
max_elem = a[0]
for elem in a:
    if elem > max_elem:
        max_elem = elem
        max_count = 1
    elif elem == max_elem:
        max_count += 1
print(f'Количество элементов, имеющих максимальное значение: {max_count}')
