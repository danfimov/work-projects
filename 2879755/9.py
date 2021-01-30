def check(string):
    result = 0
    for i in range(1, len(string),2):
        result += string[i]
    return result > 0


n1, m1 = map(int, input('Введите размерность первого массива: ').split())
matrix1 = list()
for i in range(n1):
    matrix1.append(list(map(int, input(f'Строка {i}: ').split())))

n2, m2 = map(int, input('Введите размерность второго массива: ').split())
matrix2 = list()
for i in range(n2):
    matrix2.append(list(map(int, input(f'Строка {i}: ').split())))

result_1 = 0
result_2 = 0

for string_index in range(n1):
    result_1 += check(matrix1[string_index])
for string_index in range(n2):
    result_2 += check(matrix2[string_index])

if result_1 + result_2 == 0:
    print('Нет строк, удовлетворяющих условию')
else:
    print('Количество строк первой матрицы, удовлетворяющих условию:', result_1)
    print('Количество строк второй матрицы, удовлетворяющих условию:', result_2)
