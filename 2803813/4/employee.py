from person import Person
import datetime


class Employee(Person):
    # конструктор
    def __init__(self, surname='Blank', age=10, date_of_admission=datetime.date.today().year):
        Person.__init__(self, surname, age)
        if datetime.date == type(date_of_admission):
            self.date_of_admission = date_of_admission
        else:
            try:
                date_of_admission = datetime.date(date_of_admission, 1, 1)
                self.date_of_admission = date_of_admission
            except:
                raise TypeError('Некорректный формат даты')

    def __str__(self): # приведение к строковому типу
        return f'Фамилия: {self.surname}   Возраст: {self.age}   Год поступления на работу: {self.date_of_admission.year}'

    def experience(self): # количество лет стажа
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

        return 'Cтаж: ' + str(result) + years_word(result)

    def days_of_work(self): # дней с года поступления на работу
        return 'Дней после года поступления на работу: ' + str(
            (datetime.date.today() - self.date_of_admission).days)

    def __del__(self):
        print(self.surname, 'удален из памяти')
