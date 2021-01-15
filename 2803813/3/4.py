def is_prime(number): # функция для проверки, является ли число простым
    if number == 1: return False
    # все делители, не считая 1 и самого числа, находятся на промежутке от 2 до корня из этого числа
    for potential_divisor in range(2, int(number ** 0.5) + 2):
        if number % potential_divisor == 0: # если мы нашли делитель, число явно не простое
            return False # и дальше смысла перебирать нет, поэтому сразу возрвращаем False
    return True


def prime_numbers(a, b): # основная функция поиска простых чисел
    if int != type(a) or int != type(b): # проверка корректности введенных данных
        raise TypeError('На вход переданы не целые числа')
    result = [elem for elem in range(a, b+1) if is_prime(elem)]
    return tuple(result) # приводим результат к кортежу, как сказано в задании