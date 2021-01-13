from random import randint


def print_matrix(matrix):
    for string in matrix:
        for elem in string:
            print('{:2d}'.format(elem), end=' ')
        print()


def generate_matrix(n=5, m=5):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(randint(10, 99))
    return a


matrix = generate_matrix()
print_matrix(matrix)

print()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i < j:
            matrix[i][j] = 0
print_matrix(matrix)
