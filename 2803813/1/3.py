day = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
for elem in enumerate(day):
    print(f'{elem[0] + 1}) {elem[1]} - ', end='')
    if elem[0] <= 4:
        print('рабочий')
    else:
        print('выходной')