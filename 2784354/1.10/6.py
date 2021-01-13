from random import randint


def print_matrix(matrix):
    for string in matrix:
        for elem in string:
            print(elem, end=' ')
        print()


def generate_matrix(n=5, m=5):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(randint(10, 99))
    return a


def read_matrix():
    a = []
    s = list(map(int, input().split()))
    while s:
        a.aapend(s)
        s = list(map(int, input().split()))
    return a


# можно сгенерировать матрицу
# a = generate_matrix()
# print_matrix(a)

# можно ввести с консоли
a = read_matrix()

max_elem, min_elem = a[0][0], a[0][0]
max_index, min_index = (0, 0), (0, 0)
for i, string in enumerate(a):
    for j, elem in enumerate(string):
        if max_elem < elem:
            max_elem = elem
            max_index = (i, j)
        if min_elem > elem:
            min_elem = elem
            min_index = (i, j)

print(f'Максимальный элемент массива равен {max_elem} и находится на позиции {max_index}')
print(f'Минимальный элемент массива равен {min_elem} и находится на позиции {min_index}')
