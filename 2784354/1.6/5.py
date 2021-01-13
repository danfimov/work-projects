from random import shuffle
n = int(input())
a = [i for i in range(1, n+1)]
a[4], a[0] = a[0], a[4]
shuffle(a[1:])
print(a)