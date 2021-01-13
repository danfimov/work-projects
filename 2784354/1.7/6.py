from random import randint

a = [randint(10, 99) for i in range(10)]
print(*a)
a = a[len(a) // 2 - 1::-1] + a[:len(a) // 2 - 1:-1]
print(*a)
