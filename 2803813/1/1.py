positive = 0
negative = 0

while True:
    try:
        s = float(input())
        break
    except:
        print('Некорректное число, введите новое')
        continue

while s != 0:
    if s > 0:
        positive += s
    else:
        negative += s

    while True:
        try:
            s = float(input())
            break
        except:
            print('Некорректное число, введите новое')
            continue

print('Сумма положительных', positive)
print('Сумма отрицательных', negative)
