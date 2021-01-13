import pickle


class Employee:  # сотрудник фирмы "Рога и копыта"
    name = 'empty_name'
    surname = 'empty_surname'
    post = 'empty_post'

    def __str__(self):
        return f'|{self.name} {self.surname}: {self.post}|'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname and self.post == other.post


class DataBase:  # база данных для сотрудников
    file_name = '2.3.2.txt'

    def view(self):  # чтение базы данных
        workers_db = []
        f = open(self.file_name, 'rb')
        while True:
            try:
                workers_db.append(pickle.load(f))
            except:
                break
        f.close()
        return workers_db

    def write_element(self, element):  # запись нового элемента в базу
        f = open(self.file_name, 'ab')
        pickle.dump(element, f)
        f.close()

    def delete_element(self, element):  # удаление элемента из базы
        workers_db = self.view()
        if element in workers_db:
            workers_db.remove(element)
            f = open(self.file_name, 'wb')
            for element in workers_db:
                self.write_element(element)
            print('>> Succesful delete')
        else:
            print('>> Elemrnt not in database')

    def sort(self, parameter_name):  # сортирока базы
        workers_db = self.view()
        if parameter_name == 'name':
            workers_db.sort(key=lambda x: x.name)
        elif parameter_name == 'surname':
            workers_db.sort(key=lambda x: x.surname)
        elif parameter_name == 'post':
            workers_db.sort(key=lambda x: x.post)
        else:
            print('>> Parameter not found')
        f = open(self.file_name, 'wb')
        for element in workers_db:
            pickle.dump(element, f)
        f.close()


# создаем и очищаем файл с базой данных
f = open('2.3.2.txt', 'wb')
f.close()

# моздаем нужные элементы
workers_db = DataBase()
a = Employee()
a.name, a.surname, a.post = 'Dima', 'Anfimov', 'director'
b = Employee()
b.name, b.surname, b.post = 'July', 'Markova', 'manager'
c = Employee()
c.name, c.surname, c.post = 'Mark', 'Anisimov', 'sell-manager'

# добавялем элементы в базу данных
workers_db.write_element(a)
workers_db.write_element(b)
workers_db.write_element(c)

# вывод элементов
print('Элементы базы данных:')
print(*workers_db.view())

# сортировка по фамилии
print('\nОтсортированные по фамилии элкменты базы данных:')
workers_db.sort('surname')
print(*workers_db.view())

# удаление одного из элементов
print('\nПосле удаления одного элемента:')
workers_db.delete_element(a)
print(*workers_db.view())