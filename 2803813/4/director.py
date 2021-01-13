from employee import Employee
import datetime


class Director(Employee): # класс директора
    # конструктор
    def __init__(self, surname='Blank', age=10, date_of_admission=datetime.date.today().year):
        Employee.__init__(self, surname, age, date_of_admission)

    def __str__(self):  # приведение к строковому типу (переопределено)
        return f'Фамилия: {self.surname}   Возраст: {self.age}   Должность: директор   Год поступления ' \
               f'на работу: {self.date_of_admission.year} '

    def experience(self): # количество лет стажа (переопределено)
        result = datetime.date.today().year - self.date_of_admission.year

        def years_word(years):
            if 11 <= years % 100 <= 14:
                return ' лет'
            elif 2 <= years % 10 <= 4:
                return ' года'
            elif years % 10 == 1:
                return ' год'
            else:
                return ' лет'

        return 'Директор проработал здесь ' + str(result) + years_word(result)

    def days_of_work(self): # дней с года поступления на работу (переоперделено)
        return 'Дней с вступления в должность: ' + str(
            (datetime.date.today() - self.date_of_admission).days)

    def __del__(self): # деструктор (переопредлено)
        print('Директор', self.surname, 'удален из памяти')
