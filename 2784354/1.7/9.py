def is_prime(number):
    for potential_divisor in range(2, int(number ** 0.5) + 2):
        if number % potential_divisor == 0:
            return False
    return True


a = list(map(int, input().split()))
b = [elem for elem in a if is_prime(elem)]
print(f'Простые элементы массива: {b}')
