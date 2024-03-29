from math import sin, cos, sqrt


def priority(op):
    if op in "+-": return 1
    if op in "*/": return 2
    return 100


def lastOp(s):
    minPrt = 50
    k = -1
    nest = 0
    for i in range(len(s)):
        if s[i] == '(':
            nest += 1
        elif s[i] == ')':
            nest -= 1
        elif nest == 0 and priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            k = i
    return k


def Calc(s):
    k = lastOp(s)
    if k < 0:  # вся строка - число
        if s[0] == '(':
            return Calc(s[1:-1])
        if s.startswith('abs'):
            return abs(Calc(s[4:-1]))
        if s.startswith('sin'):
            return sin(Calc(s[4:-1]))
        if s.startswith('cos'):
            return cos(Calc(s[4:-1]))
        if s.startswith('sqrt'):
            return sqrt(Calc(s[5:-1]))
        return float(s)
    else:
        n1 = Calc(s[:k])  # левая часть
        n2 = Calc(s[k + 1:])  # правая часть
        # выполнить операцию
        if s[k] == "+":
            return n1 + n2
        elif s[k] == "-":
            return n1 - n2
        elif s[k] == "*":
            return n1 * n2
        else:
            return n1 / n2
