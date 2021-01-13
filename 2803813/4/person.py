class Person:
    def __init__(self, surname='Blank', age=10):
        if str != type(surname):
            raise TypeError('Некорректный тип данных для фамилии')
        if int != type(age):
            raise TypeError('Некорректный тип данных для имени')
        self.__surname = surname # фамилия
        self.__age = age # возраст

    @property
    def surname(self): # геттер для фамилии
        return self.__surname

    @property
    def age(self): # геттер для возраста
        return self.__age

    @surname.setter  # сеттер для фамилии
    def surname(self, new_surname):
        if str != type(new_surname):
            raise TypeError('Некорректный тип данных для фамилии')
        self.__surname = new_surname

    @age.setter # сеттер для возраста
    def age(self, new_age):
        if int != new_age: raise TypeError('Некорректный тип данных для фамилии')
        if new_age in range(1, 100):
            self.__age = new_age
        else:
            raise ValueError('Недопустимый возраст')

    def __str__(self): # приведение к строковому типу
        return f'Фамилия: {self.__surname}   Возраст: {self.__age}'
