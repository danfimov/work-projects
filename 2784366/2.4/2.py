def postfix_expression(string):
    operands = '+-/*'
    opearandStack = []
    try:
        for elem in string.split():
            if elem in operands:
                second = opearandStack.pop()
                first = opearandStack.pop()
                if elem == '+':
                    opearandStack.append(first + second)
                if elem == '-':
                    opearandStack.append(first - second)
                if elem == '/':
                    opearandStack.append(first / second)
                if elem == '*':
                    opearandStack.append(first * second)
            else:
                opearandStack.append(int(elem))
    except:
        return 'Некорректное постфиксное выражение'

    if len(opearandStack) != 1:
        return 'Некорректное постфиксное выражение'
    return opearandStack.pop()


# Примеры:
# (обычное)             (постфиксное)
# (A + B) * C       =   A B + C *
# A + B * C + D     =   A B C * + D +
# (A + B) * (C + D) =   A B + C D + *
# A * B + C * D     =   A B * C D * +
# A + B + C + D     =   A B + C + D +

string = '2 4 + 6 *'
print(postfix_expression(string), '= 36')