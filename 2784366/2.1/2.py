def preparation():
    f = open('2.1.2.txt', 'w')
    for i in range(10):
        print(i * 10 ** 9 + i, file=f)
    f.close()


def long_numbers(file_name):
    f = open(file_name, 'r')
    result = []
    for line in f:
        number_array = []
        number = int(line)
        while number:
            number_array.append(number % 1000)
            number //= 1000
        result.append(number_array)
    f.close()
    return result


def print_long_numbers(number):
    for index, elem in enumerate(number):
        if index == 0:
            print(elem, end='')
        else:
            print('.{:03d}'.format(elem), end='')


# если нужен файл для подготовки - раскомментировать
# preparation()

a = long_numbers('2.1.2.txt')
for number in a:
    print_long_numbers(number)
    print()