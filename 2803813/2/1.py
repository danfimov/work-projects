with open('2.1-input.txt', 'r', newline='') as f:
    min_number, max_number = False, False
    for line in f:
        number = int(line)
        if min_number is False or min_number > number:
            min_number = number
        if max_number is False or max_number < number:
            max_number = number
with open('2.1-output.txt', 'w', newline='') as f:
    print(min_number, file=f)
    print(max_number, file=f)
