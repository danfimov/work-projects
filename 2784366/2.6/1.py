n, l = map(int,
           input('Введите количество литров в цистерне и количество ведер через пробел: ').split())
cans = list(map(int, input('Введите размеры бидонов, разделенные пробелами: ').split()))

K = [0]
for i in range(1, n + 1):
    K.append(1 + min([K[i - litres] for litres in cans if litres <= i]))
print('Общее количество бидонов:', K[n])

print('Бидоны: ', end='')
i = n
while i != 0:
    min_ltr = i
    min_cans = K[i]
    for j in range(i):
        if ((i - j) in cans) and (K[j] < min_cans):
            min_cans = K[j]
            min_index = j
    print(i - min_index, end=' ')
    i = min_index
