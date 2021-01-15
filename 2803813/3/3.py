# https://coderoad.ru/44101156/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%82%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B0-Pascal-%D0%B2-Python
def triangle(n):
    if int != type(n):
        raise TypeError('Неверный тип переменной n')
    if n < 1:
        raise ValueError('Недопустимое значение аргумента функции')
    pascal = []
    for x in range(n):
        if x == 0:
            help_list = [1]
            pascal.append(help_list)
            continue
        if x == 1:
            help_list = [1, 1]
            pascal.append(help_list)
            continue
        help_list = [l for l in range(x + 1)]
        for y in range(1, x):
            help_list[0] = 1
            help_list[x] = 1
            help_list[y] = pascal[x - 1][y] + pascal[x - 1][y - 1]
        pascal.append(help_list)
    for index, lst in enumerate(pascal):
        print('  ' * (n - index), end='')
        for elem in lst:
            print('{:<3}'.format(elem), end=' ')
        print()
