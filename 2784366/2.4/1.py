from random import randint
def preparation():
    a = [randint(10, 99) for i in range(10)]
    f = open('2.4.1.txt', 'w')
    for elem in a:
        print(elem, file = f)
    f.close()

# если нужно подготовить файл - раскомментируйте
# preparation()

f = open('2.4.1.txt', 'r')
a = []
for line in f:
    a.append(int(line))
f.close()

print(*a)
result = [a.pop() for i in range(len(a))]
print(*result)