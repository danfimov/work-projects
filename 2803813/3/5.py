def monotone(lst):
    if list != type(lst):
        raise TypeError('Передан не список')
    if len(lst) <= 2:
        return True

    lst1 = sorted(lst)
    lst2 = sorted(lst1, reverse=True)

    flag1 = True
    flag2 = True

    for i in range(len(lst)):
        if lst[i] != lst1[i]:
            flag1 = False
        if lst[i] != lst2[i]:
            flag2 = False
    return flag1 or flag2
