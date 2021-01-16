from random import randint


class TRoad:
    """
    Класс TRoad.

    Модель многополосной дороги.
    Свойства:
      length: длина дороги
      width:  ширина дороги (число полос)
    """

    def __init__(self, length0, width0):
        if length0 > 0:
            self.length = length0
        else:
            self.length = 0
        if width0 > 0:
            self.width = width0
        else:
            self.width = 0


class TCar:
    """
    Класс TCar.

    Модель автомобиля.
    Свойства:
      road:   ссылка на дорогу (объект класса TRoad)
      P:      номер полосы
      X:      координата от начала дороги
      V:      скорость в условных единицах
              (за 1 интервал моделирования)
    Методы:
      move:   продвижение за 1 интервал моделирования
    """

    def __init__(self, road0, p0, v0):
        self.road = road0
        self.P = p0
        self.V = v0
        self.X = 0

    def move(self):
        self.X += self.V
        if self.X > self.road.length:
            self.X = 0


class Tlight:
    """
    Класс Tlight

    Модель светофора.
    Свойства:
        x:          координата от начала движения
        seconds:    количество секунд с начала движения
        color:      цвет светофора в данный момент
    """

    def __init__(self, color, x=-1):
        if x < 0:
            self.__x = randint(0, road.length)
        else:
            self.__x = x
        self.__road = road
        self.__color = color
        self.__seconds = 0

    @property
    def x(self):
        return self.__x

    @property
    def color(self):
        return self.__color

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, new_seconds):
        self.__seconds = new_seconds

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def next_step(self):
        self.seconds += 1
        if self.seconds % 11 < 5:
            self.color = 'Red'
        elif self.seconds % 11 < 6:
            self.color = 'Yellow'
        else:
            self.color = 'Green'


# ------------------------------------
# Основная программа
# ------------------------------------
road = TRoad(60, 3)

N = 3
cars = []
for i in range(N):
    cars.append(TCar(road, i + 1, 2 * (i + 1)))

M = 2
lights = []
for j in range(M):
    lights.append(Tlight('Green'))


print("Дорога: длина = ", road.length, "; ширина = ", road.width, sep="")
print('Свойства светофоров:')
for j in range(M):
    print(j, ': X = ', lights[j].x, "; color = ", lights[j].color, sep='')
print("Свойства машин:")
for i in range(N):
    print(i, ": P = ", cars[i].P, "; V = ", cars[i].V, "; X = ", cars[i].X, sep="")

for k in range(100):
    for j in range(M):
        lights[j].next_step()
    for i in range(N):
        cars[i].move()

print("После 100 шагов:")
for i in range(N):
    print("X[", i, "] = ", cars[i].X, sep="")
for j in range(M):
    print("Color[", j, "] = ", lights[j].color, sep="")