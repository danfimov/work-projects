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
        help_list = [l for l in range(x + 1)]  # this will just initialize list so you can add to it
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
