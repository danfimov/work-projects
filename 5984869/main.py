# подключение необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from math import sqrt, pi

# функция для вычисления дистанции от точки до прямой
def distance_from_point_to_line(xd, yd, k, b):
    return abs(yd - k*xd - b)/(sqrt(k**2+1))

# функция для вычисления дистанции от точки до точки
def distance_from_point_to_point(x_1, y_1, x_2, y_2):
    return sqrt((x_2 - x_1)**2 + (y_2-y_1)**2)

# переводим координаты в нашу систему координат
def coordinate_change(x_answer, y_answer, sin, cos, k_2, x_per, start_in_center):
    for i in range(len(x_answer)):
        if k_2 < 0 and x_per > xt or k_2 > 0 and x_per > xt:
            x_answer[i], y_answer[i] = -x_answer[i]*cos - y_answer[i]*sin, x_answer[i]*sin - y_answer[i]*cos
        else:
            x_answer[i], y_answer[i] = x_answer[i]*cos + y_answer[i]*sin , -x_answer[i]*sin + y_answer[i]*cos

        x_answer[i] += x_center
        y_answer[i] += y_center
        if not start_in_center:
            if k_2 < 0 and x_per > xt or k_2 > 0 and x_per > xt:
                x_answer[i] +=  -b * sin
                y_answer[i] +=  b * (-cos)
            else:
                x_answer[i] += b * sin
                y_answer[i] += -b * (-cos)
    return x_answer, y_answer

# врашщение гиперболы
def hyperbole_rotation(x_answer, y_answer):
    cos90 = 0
    sin90 = 1
    for i in range(len(x_answer)):
        x_answer[i], y_answer[i] = -x_answer[i]*cos90 - y_answer[i]*sin90, x_answer[i]*sin90 - y_answer[i]*cos90
        y_answer[i] -= a
    return x_answer, y_answer

# вращение прямой
def turn_straight(x_answer, y_answer, sin, xt, yt):
    cos = (1 - sin**2)
    for i in range(len(x_answer)):
        x_answer[i], y_answer[i] = -x_answer[i]*cos - y_answer[i]*sin + xt, x_answer[i]*sin - y_answer[i]*cos + yt
    return x_answer, y_answer


# считывание параматров с консоли
print('Введите координаты точки F:')
xt,yt = map(float, input().split())
print('Введите коэффициенты для прямой d:')
k_1, b_1 = map(float, input().split())
print('Введите отношение расстояний до F и до d:')
d = float(input())

# расстояние от точки до прямой
p = distance_from_point_to_line(xt, yt, k_1, b_1)

# вычисление координат вершины параболы

# вычислим коэффициент k для нормали (перпендикуляра к прямой)
if (k_1 != 0):
    k_2 = -1/k_1
else:
    # если нормаль будет перпендикулярна оси OX
    k_2 = 1000000

# координаты точки перемечения перпендикуляра и прямой
b_2 = yt - k_2 * xt
x_per = (b_2 - b_1) / (k_1 - k_2)
y_per = k_1 * x_per + b_1

# центр новой системы координат
x_center = (xt + d*x_per)/(1+d)
y_center = (yt + d*y_per)/(1+d)

# тригонометрические функции угла поворота системы координат
cos = (0*(-1) + 1*(k_2)) / (1 * (1 + k_2**2)**0.5)
sin = (1 - cos**2)

# используемая "тема" оформления графика
plt.style.use('seaborn-whitegrid')
# показываем сетку
plt.grid = True
fig, ax = plt.subplots()

# координаты точек нормали и прямой
x_line = np.linspace(-10, 10, 100)
y_line = lambda x: k_1 * x + b_1
y_line2 = lambda x: k_2 * x + b_2
# строим прямую (красная)
ax.plot(x_line, y_line(x_line), color='r', linewidth=2)
# строим нормаль (синяя)
ax.plot(x_line, y_line2(x_line), color='b', linewidth=2)
# заданная точка
ax.scatter(xt, yt, c='b')
# пересечение нормали и прямой
ax.scatter(x_per, y_per, c='g')
# вершина параболы
ax.scatter(x_center, y_center, c='r')

# вычисляем точки для каждого из случаев
if d == 1: # парабола
    # если точка лежит на прямой, то условие соблюдается только на нормали
    if k_1 * xt + b_1 != yt:
        f = lambda x: (x) ** 2 / (2 * p)
        x_answer = np.linspace(-5, 5, 100)
        y_answer = f(x_answer)

        x_answer, y_answer = coordinate_change(x_answer, y_answer, sin, cos, k_2, x_per, True)
        ax.plot(x_answer, y_answer, color='g', linewidth=2, label='решение задачи')
    else:
        x_line = np.linspace(-10, 10, 100)
        y_line2 = lambda x: k_2 * x + b_2
        ax.plot(x_line, y_line2(x_line), color='g', linewidth=2, label='решение задачи')
elif d < 1: # эллипс
    # если точка лежит на прямой, то условие не соблюдается  нигде
    if k_1 * xt + b_1 != yt:
        rp = distance_from_point_to_point(xt, yt, x_center, y_center)  # перифокусное расстояние
        e = d  # эксцентриситет
        a = rp / (1 - e)  # большая полуось
        b = a * (1 - e ** 2) ** 0.5  # малая полуось
        # задаем точки эллипса через параметрическое уравнение
        t = np.linspace(0, 2 * pi, 200)
        x_answer = a * np.cos(t)
        y_answer = b * np.sin(t)

        x_answer, y_answer = coordinate_change(x_answer, y_answer, sin, cos, k_2, x_per, False)
        ax.plot(x_answer, y_answer, color='g', linewidth=2, label='решение задачи')

elif d > 1: # гипербола
    # если точка не лежит на прямой, то решение будет представлять собой две гиперболы, иначе - прямые
    if k_1 * xt + b_1 != yt:
        t = np.linspace(-2 * pi, 2 * pi, 200)
        e = d  # эксцентриситет
        c = p  # фокальное расстояние
        a = c / e  # б ольшая полуось
        b = sqrt(c ** 2 - a ** 2)  # малая полуось

        # первая ветвь гиперболы
        x_answer = a * np.cosh(t)
        y_answer = b * np.sinh(t)
        x_answer, y_answer = hyperbole_rotation(x_answer, y_answer)
        x_answer, y_answer = coordinate_change(x_answer, y_answer, sin, cos, k_2, x_per, True)

        ax.plot(x_answer, y_answer, color='g', linewidth=2, label='решение задачи #1')

        # вторая ветвь гиперболы
        x_answer = -a * np.cosh(t)
        y_answer = b * np.sinh(t)
        x_answer, y_answer = hyperbole_rotation(x_answer, y_answer)
        x_answer, y_answer = coordinate_change(x_answer, y_answer, sin, cos, k_2, x_per, True)

        ax.plot(x_answer, y_answer, color='g', linewidth=2, label='решение задачи #2')
    else:
        f = lambda x: k_1 * x + b_1

        # первая прямая
        x_line = np.linspace(-10, 10, 200)# интервал прорисовки прямой и количество точек
        y_line = f(x_line)
        x_line, y_line = turn_straight(x_line, y_line, 1 / d, xt, yt)
        ax.plot(x_line, y_line, color='g', linewidth=2, label='решение задачи #1')

        # вторая прямая
        x_line = np.linspace(-10, 10, 200) # интервал прорисовки прямой и количество точек
        y_line = f(x_line)
        x_line, y_line = turn_straight(x_line, y_line, -1 / d, xt, yt)
        ax.plot(x_line, y_line, color='g', linewidth=2, label='решение задачи #2')



# задаем ширину и высоту графика
fig.set_figwidth(10)  # ширина
fig.set_figheight(10)  # высота
# задаем отображаемый интервал
ax.set_ylim(-8, 8)  # у принадлежит от (-8; 8)
ax.set_xlim(-8, 8)  # х принадлежит от (-8; 8)
# настраиваем отображение легенды
ax.legend(shadow=True,  # тень от легенды
          fontsize=15,  # высота шрифта
          title_fontsize=20,  # размер шрифта заголовка
          title='Легенда:'  # заголовок
          )
# выводим график
plt.show()