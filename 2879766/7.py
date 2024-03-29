# функция для проверки условий
def check(string, string_index):  # передаем аргументами строку и её индекс
    # если строка нечетная или на втором месте стоит нечетный элемент, то условие ложно
    if string_index % 2 != 0 or string[1] % 2 != 1:
        return False

    start = string[0] % 2  # определяем, с какого элемента мы стартуем - с четного или нет
    for i in range(len(string)):
        if string[i] % 2 != start:  # сравниваем четность текущего элемента с тем, что должно быть
            return False
        # на каждом шаге цикла меняем четность проверочной переменной, ведь нам нужно чередование
        start = (start + 1) % 2
    return True  # если условия выхода не соблюлись, значит строка соответствует условиям


# считываем двумерные массивы

# просим у пользователя количество строк и столбцов
n1, m1 = map(int, input('Введите размерность первого массива: ').split())
matrix1 = list()  # изначально массив пуст пуста
for i in range(n1):  # на каждой итерации цикла добавляем новую строку в массив
    matrix1.append(list(map(int, input(f'Строка {i}: ').split())))

# аналогичные действия выполняются и со вторым массивом
n2, m2 = map(int, input('Введите размерность второго массива: ').split())
matrix2 = list()
for i in range(n2):
    matrix2.append(list(map(int, input(f'Строка {i}: ').split())))

# переменные, в которых хранится количество строк, соответствующих условию
# для кажого массива - отдельная переменная
result_1 = 0
result_2 = 0

# пробегаем по строкам и ищем нужные
for string_index in range(n1):
    result_1 += check(matrix1[string_index], string_index)
for string_index in range(n2):
    result_2 += check(matrix2[string_index], string_index)

if result_1 + result_2 == 0:  # если не нашли ни одной
    print('Нет строк, удовлетворяющих условию')
else:  # иначе пишем где и сколько строк нашли
    print('Количество строк первой матрицы, удовлетворяющих условию:', result_1)
    print('Количество строк второй матрицы, удовлетворяющих условию:', result_2)
