for number in range(10 ** 2, 10 ** 4):
    temp = number
    number_of_digits = 0
    while temp > 0:
        temp //= 10
        number_of_digits += 1

    temp = number
    sum_digits = 0
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** number_of_digits
        temp //= 10
    if sum_digits == number:
        print(number, end=' ')