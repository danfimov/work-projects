while True:  # конструкия из первой и второй задачи, чтобы проверять пользовательский ввод
    try:
        k = int(input())
        break
    except:
        print('Некорректное число, введите новое')
        continue

count = 0 # количество уже найденных магических чисел
number = 0 # перебираемое число
while count != k:
    number += 1
    temp_number = number

    sum_digits = 0
    # считаем сумму цифр, отщипывая от числа последний разряд, пока оно не обнулится
    while temp_number:
        sum_digits += temp_number % 10
        temp_number //= 10

    if sum_digits == 10: # если найдем новое магическое число
        count += 1
        if count == k: # если нашли нужное по счету магическое число
            print(number)
            break
