from person import Person
from employee import Employee
from manager import Manager
from director import Director

import datetime

a = Person('Анфимов')
print(a, end='\n\n')


b = Employee('Михайлов', 25)
print(b)
print(b.experience())
print(b.days_of_work(), end='\n\n')

f = Employee('Минько', 30, 2019)
print(f)
print(f.experience())
print(f.days_of_work(), end='\n\n')

g = Employee('Парапланов', 18, datetime.date(2010, 5, 8))
print(g)
print(g.experience())
print(g.days_of_work(), end='\n\n')

c = Director('Енотаевская', 60, 2010)
print(c)
print(c.experience())
print(c.days_of_work(), end='\n\n')

d = Manager('Эйнштейн', 30, 2005)
print(d)
print(d.experience())
print(d.days_of_work(), end='\n\n')

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

