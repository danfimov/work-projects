def dividers(number):
    for potential_divisor in range(1, number+1):
        if number % potential_divisor == 0:
            print(potential_divisor, end=' ')