def stone_sort(a, condition=lambda a, b: a > b):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if condition(a[i], a[j]):
                a[i], a[j] = a[j], a[i]
    return a


def count_digits_sum(number):
    result = 0
    while number:
        result += number % 10
        number //= 10
    return result


def condition(first, second):
    return count_digits_sum(first) < count_digits_sum(second)


a = list(map(int, input().split()))
print(*stone_sort(a, condition))
