from random import randint
from pathlib import Path

import pygame


class Shot:  # класс для пули
    def __init__(self, x, y, radius, color, facing):  # создание объекта класса
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):  # рисование объекта класса на экране
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Asteroid:
    def __init__(self, points):  # создание объекта класса
        self.x = randint(0, 340)  # координата х
        self.y = 0  # координата у

        self.image = pygame.image.load(Path('image', 'asteroid.png'))  # изображение дял астероида
        # увеличим его для удобства в 3 раза
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 3,
                                             self.image.get_height() * 3))
        # меняем размер астероида в соответствии с количеством очков пользователя
        if points <= 10:
            pass
        elif 10 < points <= 50:

            self.image = pygame.transform.scale(self.image,
                                                (round(self.image.get_width() / 2),
                                                 round(self.image.get_height() / 2)))
        elif 50 < points <= 100:
            self.image = pygame.transform.scale(self.image,
                                                (round(self.image.get_width() / 3),
                                                 round(self.image.get_height() / 3)))
        else:
            self.image = pygame.transform.scale(self.image,
                                                (round(self.image.get_width() / 4),
                                                 round(self.image.get_height() / 4)))
        # по размеру изображения получаем высоту и ширину изображения
        self.w = self.image.get_width()
        self.h = self.image.get_height()

    def draw(self, win):  # рисование объекта класса на экране
        myRect = (self.x, self.y, self.x + self.w, self.y + self.h)
        win.blit(self.image, myRect)


class Satellite:
    def __init__(self):  # создание объекта класса
        self.x = randint(0, 340)  # координата х
        self.y = 0  # координата н
        self.image = pygame.image.load(Path('image', 'satellite.png'))  # задание спутнику изображения
        # уменьшение его в 10 раз
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() // 10,
                                             self.image.get_height() // 10))
        # вычисление длины и ширины изображения
        self.w = self.image.get_width()
        self.h = self.image.get_height()

    def draw(self, win):  # рисование объекта класса на экране
        myRect = (self.x, self.y, self.x + self.w, self.y + self.h)
        win.blit(self.image, myRect)


def is_collide(bullet, other):  # функция для проверки столкновения пуль со спутниками/астероидами
    if other.y <= bullet.y <= other.y + other.h:
        if other.x <= bullet.x <= other.x + other.w:
            return True
    return False


def is_collide_rocket(x, y, other):  # функция для проверки столкновения ракеты со спутниками
    if y <= other.y + other.h:
        if x <= other.x <= x + 40:
            return True
    return False


pygame.init()  # инициализируем библиотеку
pygame.font.init()  # инициализация механизма работы с текстом
f1 = pygame.font.Font(None, 36)  # задание параметров шрифта

window = pygame.display.set_mode((400, 500))  # создадим экземпляр окна размерами 400 на 500
pygame.display.set_caption("Space Game")  # задаем заголовок окна

x = 170  # координата "х" объекта
y = 400  # координата "y" объекта
width = 40  # ширина объекта
height = 40  # высота объекта
red = (255, 0, 0)  # задаем красный цвет (RGB)
black = (0, 0, 0)  # задаем черный цвет (RGB)

# подгружаем нужные изображения
bg = pygame.image.load(Path('image', 'bg.jpg'))
walkRight = [pygame.image.load(Path('image', 'right_1.png')), pygame.image.load(Path('image', 'right_2.png')),
             pygame.image.load(Path('image', 'right_3.png')), pygame.image.load(Path('image', 'right_4.png'))]

walkLeft = [pygame.image.load(Path('image', 'left_1.png')), pygame.image.load(Path('image', 'left_2.png')),
            pygame.image.load(Path('image', 'left_3.png')), pygame.image.load(Path('image', 'left_4.png'))]

playerStand = [pygame.image.load(Path('image', 'stand_1.png')), pygame.image.load(Path('image', 'stand_2.png')),
               pygame.image.load(Path('image', 'stand_3.png'))]

left = False
right = False
animCount = 0
bullets = []  # массив для пуль

points = 0  # количество очков
asteroid = Asteroid(points)  # астероид
satellite = Satellite()  # спутник


def drawWindow():
    global animCount, x, y, asteroid, points, satellite
    window.blit(bg, (0, 0))  # размещаем в верхнем левом углу окна фоновую картинку
    text1 = f1.render('Очки: ' + str(points), True,
                      (180, 0, 0))  # задаем текст и его араметры
    window.blit(text1, (10, 30))  # располагаем текст на экране

    # анимация ракеты (из примера)
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        window.blit(walkLeft[animCount % 4], (x, y))
    elif right:
        window.blit(walkRight[animCount % 4], (x, y))
    else:
        window.blit(playerStand[animCount % 3], (x, y))
    animCount += 1

    # проверка столкновений и перерисовка пуль
    for bullet in bullets:
        if 500 > bullet.y > 25:
            bullet.y -= bullet.vel
            bullet.draw(window)

            hits = is_collide(bullet,
                              asteroid)  # вызов функции проверки столкновения пули и астероида
            if hits:
                points += 1  # доавляем очки
                bullets.pop(bullets.index(bullet))  # удаляем пулю
                asteroid = Asteroid(points)  # рисуем новый астероид сверху (и удаляем старый)

            hits = is_collide(bullet,
                              satellite)  # вызов функции проверки столкновения пули и спутника
            if hits:
                points -= 1  # отнимаем очки
                bullets.pop(bullets.index(bullet))  # удаляем пулю
                satellite = Satellite()  # рисуем новый спутник сверху (и удаляем старый)
        else:
            bullets.pop(bullets.index(bullet))

    if asteroid.y > 500:  # если астероид вышел за нижнюю границу, создаем новый
        asteroid = Asteroid(points)
    asteroid.y += 10  # двигаем астероид по вертикали
    asteroid.draw(window)  # рисуем астероид на экране

    if satellite.y > 500:  # если спутник вышел за нижнюю границу, создаем новый
        satellite = Satellite()
    satellite.y += 5  # двигаем спутник по вертикали
    satellite.x += randint(-5, 5)  # двигаем спутник по горизонтали на случайное число пикселей
    satellite.draw(window)  # рисуем спутник на экране

    hits = is_collide_rocket(x, y, satellite)  # проверяем столкновение ракеты и спутника
    if hits:
        points -= 1  # отнимаем баллы
        satellite = Satellite()  # рисуем новый спутник


# задаем состояние игры, пока эта переменная истинна будет выполняться основной цикл
condition = True

while condition:
    pygame.time.delay(100)  # задержка экрана в 100 мс.
    for event in pygame.event.get():  # перебираем все состояния из списка состояний
        # проверяем тип состояния, если это тип Quit (выход) меняем состояние на игры на False
        if event.type == pygame.QUIT:
            condition = False

    keys = pygame.key.get_pressed()  # получаем состояние всех кнопок клавиатуры
    if keys[pygame.K_LEFT] and x > 0:  # если нажата кнопка "влево"
        x -= 10  # уменьшаем координату х на 5 пикселей (двигаем объект влево)
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 400 - width:  # если нажата кнопка "вправо"
        x += 10  # увеличиваем координату х на 5 пикселей (двигаем объект вправо)
        left = False
        right = True
    else:
        left = False
        right = False

    if keys[pygame.K_SPACE]:  # выстрелы (из примера)
        if len(bullets) > 0:
            if bullets[-1].y < 350:
                bullets.append(Shot(round(x + width // 2), round(y), 5, (255, 0, 0), 1))
        else:
            bullets.append(Shot(round(x + width // 2), round(y), 5, (255, 0, 0), 1))

    drawWindow()
    pygame.display.update()
