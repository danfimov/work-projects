from random import randint
a = [randint(1000, 2000) for i in range(10)]
result = 0
for elem in a:
    result += 1 if (elem%100//10) % 2 == 0 else 0
print(result)