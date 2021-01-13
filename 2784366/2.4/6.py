# https://studref.com/324900/informatika/ispolzovanie_steka_preobrazovaniya_form_zapisi_vyrazheniy

def polska(string):
    string = string.split()

    operands = '+-/*'

    stack = []
    result = ''

    for elem in string:
        if elem == '(':
            stack.append('(')
        elif elem in operands:
            if elem == '-' or elem == '+':
                low_priority = '('
            else:
                low_priority = '(+-'

            while True:
                if len(stack) == 0:
                    break
                t = stack.pop()
                if t == '(':
                    stack.append('(')
                    break
                result = result + ' ' + t
                if t in low_priority:
                    break

            stack.append(elem)

        elif elem == ')':
            while True:
                try:
                    t = stack.pop()
                except:
                    return 'Неправильное выражение'
                if t == '(':
                    break
                else:

                    result = result + ' ' + t
        else:
            result = result + ' ' + elem
    return result + ' ' + ' '.join(stack)


# программа работает с проставленными скобками, указывающими на порядок действий

# A + B             =   A B +
print(polska('2 + 3'))
# (A + B) * C       =   A B + C *
print(polska('( 2 + 3 ) * 6'))
# A + (B * C) + D     =   A B C * + D +
print(polska('1 + ( 2 * 3 ) + 4 '))
# (A + B) * (C + D) =   A B + C D + *
print(polska('( 1 + 2 ) * ( 3 + 5 )'))