n = int(input())
for number in range(1, n+1):
    condition_is_met = True
    digits = str(number)
    temp = number
    while temp > 0:
        digit = temp%10
        temp //=10
        if digit == 0 or number % digit != 0:
            condition_is_met = False
    if condition_is_met:
        print(number, end = ' ')