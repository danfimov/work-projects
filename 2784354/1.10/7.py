# 7
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
matrix = generate_matrix()
print_matrix(matrix)

# можно ввести с консоли
# matrix = read_matrix()

string_max, string_max_index = 0, 0
for i, string in enumerate(matrix):
    string_sum = 0
    for elem in string:
        string_sum += elem
    if string_sum > string_max:
        string_max = string_sum
        string_max_index = i
print()
print(*matrix[string_max_index])