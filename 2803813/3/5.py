def monotone(lst):
    if list != type(lst): # проверка корректности введенных значений
        raise TypeError('Передан не список')
    if len(lst) <= 2: # список из двух элементов всегда является монотонным
        return True

    lst1 = sorted(lst) # отсортируем по возрастанию
    lst2 = sorted(lst1, reverse=True) # отсортируем по убыванию

    flag1 = True
    flag2 = True

    for i in range(len(lst)):
        if lst[i] != lst1[i]:
            flag1 = False
        if lst[i] != lst2[i]:
            flag2 = False
    # если по итогам оба флага будут ложны, то последовательность ни убывающая, ни возрастающая
    return flag1 or flag2
