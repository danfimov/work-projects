def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return nums


def my_sort(a):
    # для начала выписываем все строчные буквы из исходного массива
    a_lower = list()
    for elem in a:
        if elem.islower():
            a_lower.append(elem)
    # сортируем массив строчных обычной сортировкой пузырьком
    a_lower = bubble_sort(a_lower)
    # вставляем на нужных местах отсортированные строчные буквы
    j = 0
    for index in range(len(a)):
        if a[index].islower():
            a[index] = a_lower[j]
            j += 1
    return a


result_arrays = []
unmodified_arrays = 0
for array_index in range(1, 6):  # ввод пяти массивов
    user_input = list(input(f'Введите массив №{array_index}: ').split())

    user_input_sorted = my_sort(user_input.copy())  # записываем преобразованный массив
    # добавляем в результрующую переменную, чтобы вывести все массивы по окончании работы программы
    result_arrays.append(user_input_sorted)

    # осуществляем проверку на равенство изначального и преобразованного массивов
    is_similar = True
    for i in range(len(user_input)):
        if user_input[i] != user_input_sorted[i]:
            is_similar = False
            break

    unmodified_arrays += int(is_similar)

if unmodified_arrays == 5:
    print('Исходные массивы удовлетворяют требуемому условию')
else:
    for i in range(0, 5):
        print(f'Преобразованный массив №{i + 1}:', *result_arrays[i])
