while True:  # та же конструкцию, что и в предыдущей задаче
    try:
        n = int(input())
        break
    except:
        print('Некорректное число, введите новое')
        continue

for number in range(1, n + 1):
    # len(str(number)) - по факту, количество символов в числе

    # нам останется лишь поделить квадрат числа на нужную степень десятки,
    # чтобы отщипнуть нужное количество разрядов
    if number == (number * number) % (10 ** len(str(number))):
        print(number)
