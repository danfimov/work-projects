def is_prime(number):
    for potential_divisor in range(2, int(number**0.5)+2):
        if number % potential_divisor == 0:
            return False
    return True

def hyperprime(number):
    while number:
        if not is_prime(number):
            return False
        number //= 10
    return True