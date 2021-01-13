from random import randint


def print_matrix(matrix):
    for string in matrix:
        for elem in string:
            print('{:<2d}'.format(elem), end=' ')
        print()


def generate_matrix(n=5, m=5):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(randint(10, 99))
    return a


def transposition(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([0 for i in range(len(matrix))])

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[j][i] = matrix[i][j]
    return result


matrix = generate_matrix()
print_matrix(matrix)
print()

matrix = transposition(matrix)
print_matrix(matrix)
