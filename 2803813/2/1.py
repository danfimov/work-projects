with open('2.1-input.txt', 'r', newline='') as f: # считываем данные из файла
    min_number, max_number = False, False # пока не нашли ни максимального, ни минимального
    for line in f:
        number = int(line)
        if min_number is False or min_number > number: # проверяем, что не минимум-ли число
            min_number = number
        if max_number is False or max_number < number: # проверяем, что не максимум-ли число
            max_number = number
with open('2.1-output.txt', 'w', newline='') as f: # производим запись ответа в другой файл
    print(min_number, file=f)
    print(max_number, file=f)
