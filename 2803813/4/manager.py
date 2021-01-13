from employee import Employee
import datetime


class Manager(Employee):  # класс менеджера
    # конструктор
    def __init__(self, surname='Blank', age=10, date_of_admission=datetime.date.today().year):
        Employee.__init__(self, surname, age, date_of_admission)

    def __str__(self):  # приведение к строковому типу (переопределено)
        return f'Фамилия: {self.surname}   Возраст: {self.age}   Должность: менеджер   Год поступления на работу: {self.date_of_admission.year}'
    # не переопределены остальные методы родительского класса
