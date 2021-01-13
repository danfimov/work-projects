def sum_digits(number):
    result = 0
    while number:
        result += number%10
        number //= 10
    return result