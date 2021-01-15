import datetime
import pickle
from my_exception import ExperienceException

# общий файл для всех классов из предыдущей лабораторной
# из нового: два метода в Person и два - в Employee

class Person:
    def __init__(self, surname='Blank', age=10):
        if str != type(surname):
            raise TypeError(f'Некорректный тип данных для фамилии ')
        if int != type(age):
            raise TypeError('Некорректный тип данных для имени')
        self.__surname = surname
        self.__age = age

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @surname.setter
    def surname(self, new_surname):
        if str != type(new_surname):
            raise TypeError('Некорректный тип данных для фамилии')
        self.__surname = new_surname

    @age.setter
    def age(self, new_age):
        if int != type(new_age): raise TypeError(f'Некорректный тип данных для возраста')
        if new_age in range(1, 100):
            self.__age = new_age
        else:
            raise ValueError('Недопустимый возраст')

    def __str__(self):
        return f'Фамилия: {self.__surname}   Возраст: {self.__age}'

    def to_binary(self, filepath):  # записать данные в бинарный файл
        try:
            with open(filepath, 'wb') as file:
                pickle.dump(self, file)
        except IOError as e:
            print('Ошибка записи в файл: ', e)
        except Exception as e:
            print('Некорректные данные: ', e)

    def from_binary(self, filepath):  # взять данные из бинарного файла
        try:
            with open(filepath, 'rb') as file:
                other_person = pickle.load(file)
                self.surname = other_person.surname
                self.age = other_person.age
        except IOError as e:
            print('Ошибка записи в файл: ', e)
        except Exception as e:
            print('Некорректные данные: ', e)


class Employee(Person):
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

    def __str__(self):
        return f'Фамилия: {self.surname}   Возраст: {self.age}   Год поступления на работу: {self.date_of_admission.year}'

    def experience(self):
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

        return 'Стаж: ' + str(result) + years_word(result)

    def days_of_work(self):
        return 'Дней после года поступления на работу: ' + str(
            (datetime.date.today() - self.date_of_admission).days)

    def __del__(self):
        print(self.surname, 'удален из памяти')

    def to_binary(self, filepath):  # записать данные в бинарный файл
        try:
            with open(filepath, 'wb') as file:
                pickle.dump(self, file)
        except IOError as e:
            print('Ошибка записи в файл: ', e)
        except Exception as e:
            print('Некорректные данные: ', e)

    def from_binary(self, filepath):  # взять данные из бинарного файла
        try:
            with open(filepath, 'rb') as file:
                other_person = pickle.load(file)
                if not isinstance(other_person, Employee):
                    raise ExperienceException()
                self.surname = other_person.surname
                self.age = other_person.age
                self.date_of_admission = other_person.date_of_admission
        except ExperienceException as e:
            print('Пользовательское исключение:', e.txt)
        except IOError as e:
            print('Ошибка записи в файл: ', e)

        except Exception as e:
            print('Некорректные данные: ', e)


class Director(Employee):
    def __init__(self, surname='Blank', age=18, date_of_admission=datetime.date.today().year):
        Employee.__init__(self, surname, age, date_of_admission)

    def __str__(self):
        return f'Фамилия: {self.surname}   Возраст: {self.age}   Должность: директор   Год поступления ' \
               f'на работу: {self.date_of_admission.year} '

    def experience(self):
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

    def days_of_work(self):
        return 'Дней с вступления в должность: ' + str(
            (datetime.date.today() - self.date_of_admission).days)

    def __del__(self):
        print('Директор', self.surname, 'удален из памяти')


class Manager(Employee):
    def __init__(self, surname='Blank', age=10, date_of_admission=datetime.date.today().year):
        Employee.__init__(self, surname, age, date_of_admission)

    def __str__(self):
        return f'Фамилия: {self.surname}   Возраст: {self.age}   Должность: менеджер   Год поступления на работу: {self.date_of_admission.year}'
