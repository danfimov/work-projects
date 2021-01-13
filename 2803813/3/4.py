def is_prime(number):
    if number == 1: return False
    for potential_divisor in range(2, int(number ** 0.5) + 2):
        if number % potential_divisor == 0:
            return False
    return True


def prime_numbers(a, b):
    if int != type(a) or int != type(b):
        raise TypeError('На вход переданы не целые числа')
    result = [elem for elem in range(a, b+1) if is_prime(elem)]
    return tuple(result)