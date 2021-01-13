from random import randint
a = [randint(10, 99) for i in range(10)]
k, m = map(int, input().split())
print(*a)
print(*a[m:k-1:-1])
a = a[:k] + a[k:m+1][::-1] + a[m+1:]
print(*a)