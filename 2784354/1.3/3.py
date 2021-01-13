a, b, c, d, e = map(int, input().split())

# вариация сортировки пузырьком без списков и циклов

# большие числа как бы всплываю вверх до тех пор, пока выше них не окажется еще
# более крупное число
if b > a:
    a, b = b, a

if c > b:
    b, c = c, b
    if b > a:
        a, b = b, a

if d > c:
    c, d = d, c
    if c > b:
        b, c = c, b
        if b > a:
            a, b = b, a

if e > d:
    e, d = d, e
    if d > c:
        c, d = d, c
        if c > b:
            b, c = c, b
            if b > a:
                a, b = b, a

print(f'Максимум = {a}, минимум = {d}')