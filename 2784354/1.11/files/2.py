from random import randint


# подготовка исходного файла, если нужно
def generate_file():
    f = open('1.2.txt', 'w')
    a = [randint(0, 100) for i in range(10)]
    print(*a, sep='\n', end='', file=f)
    f.close()


def stone_sort(a, condition=lambda a, b: a % 10 > b % 10):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if condition(a[i], a[j]):
                a[i], a[j] = a[j], a[i]
    return a


# generate_file()
f = open('1.2.txt', 'r')
result = open('1.2-result.txt', 'w')

a = []
for line in f:
    a.append(int(line))
print(*stone_sort(a), sep='\n', end='', file=result)

f.close()
result.close()
