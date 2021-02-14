todo_list = list(input().split(', '))  # считываем список дел
print(*todo_list[::2], sep=', ')
print(*todo_list[1::2], sep=', ')
