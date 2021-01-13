# 220 и 284 (Пифагор, около 500 до н. э.)
# 1184 и 1210 (Паганини, 1860)
# 2620 и 2924 (Эйлер, 1747)
# 5020 и 5564 (Эйлер, 1747)
# 6232 и 6368 (Эйлер, 1750)


def sum_of_divisors(number):
    result = 0
    for potential_divisor in range(1, number):
        if number % potential_divisor == 0:
            result += potential_divisor
    return result


# медленно находит дружественные числа
for i in range(1, 10000):
    for j in range(i + 1, 10000):
        if sum_of_divisors(i) == j and i == sum_of_divisors(j):
            print(i, j)

# такая программа будет работать быстрее, так как мы запоминаем суммы делителей заранее
a = [sum_of_divisors(i) for i in range(10000)]
for i in range(1, 10000):
    for j in range(i + 1, 10000):
        if a[i] == j and i == a[j]:
            print(i, j)