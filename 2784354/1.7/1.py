a = list(map(int, input().split()))
max_pos = 0
min_pos = a[0]
for elem in a:
    if elem > 0 and elem % 2 == 0:
        if max_pos < elem: max_pos = elem
        if min_pos > elem: min_pos = elem

if max_pos == 0:
    print('Нет четных положительных')
else:
    print(f'Максимальный четный положительный {max_pos}')
    print(f'Минимальный четный положительный {min_pos}')
