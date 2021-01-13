a, b = map(int, input().split())
for number in range(a, b+1):
    is_prime = True
    for potential_divisor in range(2, int(number**0.5)+2):
        if number % potential_divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=' ')