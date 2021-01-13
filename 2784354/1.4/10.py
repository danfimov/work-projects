n = int(input())
for number in range(1, n+1):
    number_of_digits = 0
    temp = number
    while temp > 0:
        temp //= 10
        number_of_digits += 1
    if number**2 % 10**number_of_digits == number:
        print(number, end=' ')