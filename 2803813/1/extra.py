
while True:
    try:
        k = int(input())
        break
    except:
        print('Некорректное число, введите новое')
        continue

count = 0
number = 0
while count != k:
    number += 1
    temp_number = number

    sum_digits = 0
    while temp_number:
        sum_digits += temp_number % 10
        temp_number //= 10

    if sum_digits == 10:
        count += 1
        if count == k:
            print(number)
            break