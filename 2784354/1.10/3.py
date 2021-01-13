def stone_sort(a, condition=lambda a, b: a > b):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if condition(a[i], a[j]):
                a[i], a[j] = a[j], a[i]
    return a


a = list(map(int, input().split()))
a = stone_sort(a[:len(a) // 2]) + stone_sort(a[len(a) // 2:], lambda a, b: a < b)
print(*a)
