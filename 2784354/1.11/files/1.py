from random import randint


# подготовка исходного файла, если нужно
def generate_file():
    f = open('1.1.txt', 'w')
    a = [randint(0, 100) for i in range(10)]
    print(*a, sep='\n', end='', file=f)
    f.close()


# generate_file()
f = open('1.1.txt', 'r')
result = open('1.1-result.txt', 'w')
sum_numbers = 0
count_numbers = 0
for line in f:
    sum_numbers += int(line)
    count_numbers += 1
print(sum_numbers / count_numbers, file=result)

f.close()
result.close()
