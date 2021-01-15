from test import *


# блок кода с пользовательским вводом из предыдущей лабораторной
who = input('Кого вы хотите создать? (человек/работник/директор/менеджер) ').strip()
if who == 'человек':
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    e = Person(surname, age)
    print(e, end='\n\n')
elif who == 'работник':
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    year = int(input('Введите год поступления на работу: '))
    e = Employee(surname, age, year)
    print(e)
    print(e.experience())
    print(e.days_of_work(), end='\n\n')
elif who == 'директор':
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    year = int(input('Введите год поступления на работу: '))
    e = Director(surname, age, year)
    print(e)
    print(e.experience())
    print(e.days_of_work(), end='\n\n')
elif who == 'менеджер':
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    year = int(input('Введите год поступления на работу: '))
    e = Manager(surname, age, year)
    print(e)
    print(e.experience())
    print(e.days_of_work(), end='\n\n')



