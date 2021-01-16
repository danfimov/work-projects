from random import randint


class TRoad:
    """
    Класс TRoad.

    Модель многополосной дороги.
    Свойства:
      length: длина дороги
      width:  ширина дороги (число полос)
    """

    def __init__(self, length0, width0, num_lights=2):
        if length0 > 0:
            self.__length = length0
        else:
            self.__length = 0
        if width0 > 0:
            self.__width = width0
        else:
            self.__width = 0

        self.__lights = []
        for light in range(num_lights):
            colors = ['Green', 'Yellow', 'Red']
            color_index = randint(0, 2)
            self.__lights.append(Tlight(self, colors[color_index]))

    @property
    def lights(self):
        return self.__lights

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    def nearest_traffic_light(self, x_car):
        min_distance = self.width + 1
        nearest = self.lights[0]
        for index in range(len(self.lights)):
            distance = self.lights[index].x - x_car
            if distance >= 0:
                if min_distance > distance:
                    min_distance = distance
                    nearest = self.lights[index]
        return nearest, min_distance


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
        self.__P = p0
        self.__V = v0
        self.__X = 0

    @property
    def P(self):
        return self.__P

    @property
    def V(self):
        return self.__V

    @property
    def X(self):
        return self.__X

    @X.setter
    def X(self, other_x):
        self.__X = other_x

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

    def __init__(self, road, color, x=-1):
        if x < 0:
            self.__x = randint(0, road.length)
        else:
            self.__x = x
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
M = 2
road = TRoad(60, 3, M)

N = 3
cars = []
for i in range(N):
    cars.append(TCar(road, i + 1, 2 * (i + 1)))

print("Дорога: длина = ", road.length, "; ширина = ", road.width, sep="")
print('Свойства светофоров:')
for j in range(M):
    print(j, ': X = ', road.lights[j].x, "; color = ", road.lights[j].color, sep='')
print("Свойства машин:")
for i in range(N):
    print(i, ": P = ", cars[i].P, "; V = ", cars[i].V, "; X = ", cars[i].X, sep="")

for k in range(99):
    for j in range(M):
        road.lights[j].next_step()
    for i in range(N):
        nearest_light, dist = cars[i].road.nearest_traffic_light(cars[i].X)
        if nearest_light.color == 'Red':
            pass  # машина стоит этот ход
        else:
            cars[i].move()

print("После 100 шагов:")
for i in range(N):
    print("X[", i, "] = ", cars[i].X, sep="")
for j in range(M):
    print("Color[", j, "] = ", road.lights[j].color, sep="")
