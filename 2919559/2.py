todo_list = list(input().split(', '))  # считываем список дел
todo_sasha, todo_zhenya = [], []  # создаем два пустых списка
for i in range(len(todo_list)):  # бежим по индексам из списка (начиная с 0)
    if i % 2 == 0:  # если индекс четный, то добавляем дело в список Жени...
        todo_sasha.append(todo_list[i])
    else:  # ...иначе - в список Саши
        todo_zhenya.append(todo_list[i])
# печатаем списки
print(*todo_sasha, sep=', ')
print(*todo_zhenya, sep=', ')