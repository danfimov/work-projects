a = set()
b = set()
with open('2.4.1-input.txt', 'r', newline='') as f: # данные из первого файла
    for line in f:
        for word in line.split():
            a.add(word)
with open('2.4.2-input.txt', 'r', newline='') as f:# данные из второго файла
    for line in f:
        for word in line.split():
            b.add(word)

with open('2.4-output.txt', 'w', newline='') as f: # запись ответа
    # функция difference как раз предоставляет нужный функционал - разность множеств
    print(*b.difference(a), file=f)


