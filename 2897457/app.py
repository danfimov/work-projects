from operator import itemgetter  # для сортировки
from re import match  # для проверки логина

from flask import Flask, render_template, request, redirect

import database  # отдельный файл с функциями для работы с БД

app = Flask(__name__)

# создание базы данных (если таковой еще нет)
connection = database.connect()
database.create_tables(connection)


# Если нужно будет изменить вопросы, то удалите базу данных data.db, измените функцию create_test
# и раскомментируйте код ниже

# database.create_test(connection)

# функция осуществляющая валидацию при входе
def validation_enter(login, password):
    connection = database.connect()
    database_answer = database.get_user_by_login(connection, login)
    if database_answer:
        if database_answer[0][2] != password:
            return False, 'Неверный пароль'
    else:
        return False, 'Нет такого логина'
    return True, ''


# функция осуществляющая валидацию при регистрации
def validation_reg(login, password, password_check):
    connection = database.connect()

    if len(database.get_user_by_login(connection, login)) > 0:
        return False, 'Пользователь с таким ником уже существует'
    if password_check != password:
        return False, 'Пароли не совпадают'
    if len(password) < 8:
        return False, 'Ненадежный пароль'
    if not match(r'[a-zA-Z0-9]', login):
        return False, 'Логин должен состоять только из английских букв и цифр'
    return True, ''


# стартовая страница (она всегда переадресовывает на вход, а уже на входе решается,
# куда нужно реально перекинуть пользователя
@app.route('/')
def main_page():
    return redirect('/enter')


# страница с авторизацией
@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':  # если мы получили ответ от формы авторизации
        login = request.form.get('login')
        password = request.form.get('password')
        is_valid, error_text = validation_enter(login, password)
        if is_valid:
            res = redirect('/test')
            # добавляем пользователю куки, чтобы знать, что он вошел
            res.set_cookie('test_login', login)
            return res
        else:
            return render_template('enter.html', error=(True, error_text),
                                   reg_link='/reg')

    if not request.cookies.get('test_login'):  # если пользователь не зарегистрирован
        return render_template('enter.html', error=(False, ''),
                               reg_link='/reg')
    else:  # если регистрация уже пройдена - переход на тест
        return redirect('/test')


# страница регистрации
@app.route('/reg', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # если получили ответ от формы регистрации
        login = request.form.get('login')
        password = request.form.get('password')
        password_check = request.form.get('password_check')
        print('DATA: ', login, password, password_check)
        is_valid, error_text = validation_reg(login, password, password_check)
        if is_valid:  # надо проверить: валидны ли данные
            connection = database.connect()
            database.add_user(connection, login, password)  # заносим нового пользователя в БД
            return redirect('/enter')
        else:  # если не валидны, выводим ошибку
            return render_template('reg.html', error=(True, error_text))
    return render_template('reg.html', error=(False, ''))


# тест
@app.route('/test', methods=['GET', 'POST'])
def test():
    login = request.cookies.get('test_login')
    connection = database.connect()

    if not login:  # если сюда попал неавторизированный пользователь, то переход на страницу с входом
        return redirect('/enter')
    if request.method == 'POST':
        if 'exit' in request.form:  # если нажали на кнопку выхода
            res = redirect('/enter')
            res.set_cookie('test_login', '', max_age=0)  # удаление куки о пользователе
            return res
        else:  # если получили ответ от формы (от теста)
            points = 0
            answers = []

            questions = database.get_all_questions(connection)  # получаем все вопросы с ответами
            for question in questions:
                id, correct_answer = str(question[0]), str(question[6])
                answer = request.form.get(id)  # берем ответ из формы
                answers.append(answer)
                if answer == correct_answer:  # сравниваем ответ с верным
                    points += 1
            # добавляем результаты в БД
            database.add_result(connection, login, ' '.join(answers), points)
            return redirect('/results')
    else:
        test = database.get_all_questions(connection)
        return render_template('test.html', login=login, test=test)


# страница с результатами
@app.route('/results', methods=['GET', 'POST'])
def result():
    login = request.cookies.get('test_login')
    if not login:  # если пользователь не вошел на сайт - переносим на страницу входа
        return redirect('/enter')
    connection = database.connect()
    results = database.get_all_results(connection)  # забираем из БД все результаты
    results = [elem[1:] for elem in results]  # убираем столбик id
    heading = ['Логин', 'Ответы', 'Баллы']  # задаем подпись столбов к таблице
    # выводим на страницу данные об ответивших в порядке убыванию баллов
    return render_template('results.html', heading=heading,
                           results=reversed(sorted(results, key=itemgetter(2, 0, 1))))


if __name__ == '__main__':
    app.debug = True
    app.run()  # запуск приложения
