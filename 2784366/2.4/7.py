def preporation():
    f = open('2.4.7.txt', 'w')
    n = 5
    for i in range(n):
        print('w' * n, file=f)
    f.close()


# если нужно подготовить матрицу - раскомментируйте
# preporation()


f = open('2.4.7.txt', 'r')
a = []
for index, line in enumerate(f):
    a.append([])
    line = line.strip()
    for elem in line:
        a[index].append(elem)
f.close()
print('Введите координаты точек в матрице и цвет')

s = input()
queue = []
while s:
    x, y, c = s.split()
    x = int(x)
    y = int(y)
    queue.append((x, y, c))
    if x < len(a) and y < len(a[x]):
        a[x][y] = c
    s = input()
while queue:
    x, y, c = queue[0]
    if x < len(a) and y < len(a[x]):
        a[x][y] = c
    queue = queue[1:]

for line in a:
    for elem in line:
        print(elem, end=' ')
    print()