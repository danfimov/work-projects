def digits(number):
    number_of_digits = 0
    temp = number
    while temp > 0:
        temp //= 10
        number_of_digits += 1
    while number:
        number_of_digits -= 1
        print(number // 10**(number_of_digits))
        number %= 10**(number_of_digits)