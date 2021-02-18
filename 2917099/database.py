import sqlite3

# все команды для взаимодействия с БД
CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, login TEXT, password TEXT);"
CREATE_TEST_TABLE = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, question TEXT, answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT, correct_answer INTEGER);"
CREATE_RESULT_TABLE = "CREATE TABLE IF NOT EXISTS results(id INTEGER PRIMARY KEY, login TEXT, answers TEXT, points INT);"

INSERT_QUESTION = "INSERT INTO test (question, answer1, answer2, answer3, answer4, correct_answer) VALUES (?, ?, ?, ?, ?, ?);"
INSERT_USER = "INSERT INTO users (login, password) VALUES (?, ?)"
INSERT_RESULT = "INSERT INTO results(login, answers, points) VALUES (?, ?, ?)"

GET_ALL_QUESTIONS = "SELECT * FROM test"
GET_ALL_USERS = "SELECT * FROM users"
GET_ALL_RESULS = "SELECT * FROM results"

GET_USER_BY_LOGIN = "SELECT * FROM users WHERE login = ?;"


# создание связи с БД
def connect():
    return sqlite3.connect('data.db')


# создание таблиц
def create_tables(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_TEST_TABLE)
        connection.execute(CREATE_RESULT_TABLE)


# добавление нового вопроса с 4 возможными ответами, где правильный лишь 1
def add_question(connection, question, answer1, answer2, answer3, answer4, correct_answer):
    with connection:
        connection.execute(INSERT_QUESTION,
                           (question, answer1, answer2, answer3, answer4, correct_answer))


# добавление нового пользователя
def add_user(connection, login, password):
    with connection:
        connection.execute(INSERT_USER, (login, password))


# добавление нового результата теста
def add_result(connection, login, answers, points):
    with connection:
        connection.execute(INSERT_RESULT, (login, answers, points))


# получение списка всех пользователей
def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()


# получение списка всех вопросов с ответами
def get_all_questions(connection):
    with connection:
        return connection.execute(GET_ALL_QUESTIONS).fetchall()


# получение всех результатов
def get_all_results(connection):
    with connection:
        return connection.execute(GET_ALL_RESULS).fetchall()


# получение пользователя по логину
def get_user_by_login(connection, login):
    with connection:
        return connection.execute(GET_USER_BY_LOGIN, (login,)).fetchall()


# создание теста с вопросами
def create_test(connection):
    with connection:
        add_question(connection, 'Переведите число 16 в двоичную систему счисления', '1000', '01111',
                     '10000', '10001', 3)
        add_question(connection, 'Переведите число 36 в систему счисления с основанием 16', '100100',
                     '24',
                     '44', '210', 2)
        add_question(connection, 'Как называется связный граф без циклов?', 'береза', 'тополь',
                     'тополь-М', 'дерево', 4)
        add_question(connection,
                     'Как называется граф, с каждым ребром которого связано некоторое число?',
                     'взвешенный', 'ориентированный',
                     'числовой', 'дерево', 1)
        add_question(connection,
                     'Как называется ребро графа, которое начинается и заканчивается в одной и той же вершине?',
                     'петля', 'Петля времени',
                     'Looper', '2012', 1)
