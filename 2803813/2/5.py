dictionary = dict()

# можно взять файл 2.5.2-input.txt для демонстрации работы с файлами разной длины
with open('2.5.1-input.txt', 'r', newline='') as f:
    for line in f: # построчно читаем файл
        for elem in line:  # побуквенно идем по строке
            if elem.isalpha(): # если символ является буквой
                elem = elem.lower() # всё к нижнему регистру, чтобы в словаре не было букв разных регистров
                if elem in dictionary: # если элемент уже есть в словаре, просто увеличиваем счетчик
                    dictionary[elem] += 1
                else: # иначе добавляем соответвующую пару ключ-значение в словарь
                    dictionary[elem] = 1

result = [(key, dictionary[key]) for key in dictionary.keys()]
result.sort(key=lambda x: x[1], reverse=True) # выполнеяем сортировку по частоте
with open('2.5-output.txt', 'w', newline='') as f: # вывод ответа в файл
    for elem in result:
        print(elem[0], elem[1],file=f)

