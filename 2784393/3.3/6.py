from itertools import product


class TLogElement:
    """
    Класс TLogElement

    Базовый класс для иерархии классов логических элементов
    Абстрактный класс.
    Свойства:
      In1 - первый вход
      In2 - второй вход
      Res - выход
    Методы:
      calc - вычисление выхода, абстрактный метод
      link - установить связь выхода со следующим элементом в схеме
    """

    def __init__(self):
        self.__in1 = False
        self.__in2 = False
        self._res = False
        self.__nextEl = None
        self.__nextIn = 0
        if not hasattr(self, "calc"):
            raise NotImplementedError

    def __setIn1(self, newIn1):
        self.__in1 = newIn1
        self.calc()
        if self.__nextEl:
            if self.__nextIn == 1:
                self.__nextEl.In1 = self._res
            elif self.__nextIn == 2:
                self.__nextEl.In2 = self._res

    def __setIn2(self, newIn2):
        self.__in2 = newIn2
        self.calc()
        if self.__nextEl:
            if self.__nextIn == 1:
                self.__nextEl.In1 = self._res
            elif self.__nextIn == 2:
                self.__nextEl.In2 = self._res

    def link(self, nextEl, nextIn):
        self.__nextEl = nextEl
        self.__nextIn = nextIn

    In1 = property(lambda x: x.__in1, __setIn1)
    In2 = property(lambda x: x.__in2, __setIn2)
    Res = property(lambda x: x._res)


class TNot(TLogElement):
    """
    Класс TNot(TLogElement)

    Элемент 'НЕ'.
    Методы:
      calc - вычисление выхода
    """

    def __init__(self):
        TLogElement.__init__(self)

    def calc(self):
        self._res = not self.In1


class TLog2In(TLogElement):
    """
    Класс TLog2In(TLogElement)

    Базовый класс для иерархии классов логических элементов
    с двумя входами.
    """
    pass


class TAnd(TLog2In):
    """
    Класс TAnd(TLog2In)

    Элемент 'И'.
    Методы:
      calc - вычисление выхода
    """

    def __init__(self):
        TLog2In.__init__(self)

    def calc(self):
        self._res = self.In1 and self.In2


class TOr(TLog2In):
    """
    Класс TOr(TLog2In)

    Элемент 'ИЛИ'.
    Методы:
      calc - вычисление выхода
    """

    def __init__(self):
        TLog2In.__init__(self)

    def calc(self):
        self._res = self.In1 or self.In2


class TXor(TLog2In):
    """
    Класс TXor(TLog2In)

    Элемент 'исключающее ИЛИ'.
    Методы:
      calc - вычисление выхода
    """

    def __init__(self):
        TLog2In.__init__(self)

    def calc(self):
        self._res = self.In1 != self.In2


class TNotAnd(TLog2In):
    """
    Класс TNotAnd(TLog2In)

    Элемент 'И-НЕ'.
    Методы:
      calc - вычисление выхода
    """

    def __init__(self):
        TLog2In.__init__(self)

    def calc(self):
        self._res = not (self.In1 and self.In2)
        return self._res


class TNotOr(TLog2In):
    """
    Класс TNotOr(TLog2In)

    Элемент 'ИЛИ-НЕ'.
    Методы:
      calc - вычисление выхода
    """

    def __init__(self):
        TLog2In.__init__(self)

    def calc(self):
        self._res = not (self.In1 or self.In2)
        return self._res


def my_trigger(State, R, S):
    a1 = TNotOr()
    a1.In1 = S
    a1.In2 = State

    a2 = TNotOr()
    a2.In1 = R
    a2.In2 = a1.Res
    return a2.Res


if __name__ == "__main__":
    print('State : R, S -> new_state')
    # нагенерируем все возможные комбинации переменных с помощью функции product
    for state, r, s in product((False, True), repeat=3):
        print('{!s:5} : {!s:5}, {!s:5} -> {!s:5}'.format(state, r, s, my_trigger(state, r, s)))