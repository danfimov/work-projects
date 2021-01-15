from humans import *

## тесты запускаются автоматическип при запуске  main.py

# если запустить код с флагом командной строки -O, то __debug__ станет равным False
# в таком случае тесты не запустятся
if __debug__:
    print('--- Тесты запущены ---')

    # тест на корректность подсчета стажа
    a = Employee('Анфимов', 38, 2001)
    assert a.experience() == 'Стаж: 20 лет', 'Не пройден тест №1'

    # тест на корректность выгрузки данных в файл и получения их обратно
    a = Person('Фамилия', 28)
    a.to_binary('person.txt')
    b = Person('Фамилия2', 30)
    b.from_binary('person.txt')
    assert b.surname == 'Фамилия', 'Не пройден тест №2'
    assert a.surname == 'Фамилия', 'Не пройден тест №3'

    # тест, где вызывается несозданный файл
    b = Person('Фамилия2', 30)
    b.from_binary('wrong_person.txt') # правоцируем ошибку записи в файл
    assert b.surname == 'Фамилия2' and b.age == 30, 'Не пройден тест №4'

    # тест, где мы пытаемся записать данные из объекта класса Person в Employee, но не находим стаж
    a = Person('Фамилия1', 28)
    a.to_binary('person.txt')
    b = Employee('Фамилия2', 30, 2005)
    b.from_binary('person.txt') # правоцируем пользовательскую ошибку
    assert b.surname == 'Фамилия2' and b.age == 30, 'Не пройден тест №5'

    a = Employee('Фамилия1', 28)
    a.to_binary('employee.txt')
    b = Director('Фамилия2', 30, 2005)
    b.from_binary('employee.txt')
    assert b.surname == 'Фамилия1' and b.age == 28, 'Не пройден тест №6'

    print('--- Тесты завершены ---\n\n')
