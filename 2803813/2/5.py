dictionary = dict()

# можно взять файл 2.5.2-input.txt
with open('2.5.1-input.txt', 'r', newline='') as f:
    for line in f:
        for elem in line:
            if elem.isalpha():
                elem = elem.lower()
                if elem in dictionary:
                    dictionary[elem] += 1
                else:
                    dictionary[elem] = 1

result = [(key, dictionary[key]) for key in dictionary.keys()]
result.sort(key=lambda x: x[1], reverse=True)
with open('2.5-output.txt', 'w', newline='') as f:
    for elem in result:
        print(elem[0], elem[1],file=f)

