from random import randint


def binary_search(a, value):
    steps = 1
    a.sort()
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        steps += 1
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return steps


a = [randint(0, 100) for i in range(32)]

result = 0
for i in range(1000):
    number = randint(0, 100)
    result += binary_search(a, number)

# по факту сложность должна быть порядка log2(100) = 6.64

# но определенная погрешность у нас безусловно будет (скорее всего сложность будет меньше),
# хотя бы исходя из того, что мы берем изначально числа из правильного диапазона
print(result / 1000)
