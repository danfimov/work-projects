def is_coorect(string):
    stack = ''
    for index, elem in enumerate(string):
        if elem in '(<[{':
            stack = stack + elem
        else:
            if len(stack) != 0:
                pair = stack[-1]
                scobki = pair + elem
                if scobki == '()' or scobki == '{}' or scobki == '[]' or scobki == '<>':
                    stack = stack[:-1]
                else:
                    print('Ошибочный символ под индексом', index)
                    return False
            else:
                print('Ошибочный символ под индексом', index)
                return False
    if stack:
        print('Скобочная последовательность не завершена')
        return False
    else:
        return True


# True
print(is_coorect(''))
print(is_coorect('()'))
print(is_coorect('{()}'))
print(is_coorect('(())'))

# False
print(is_coorect('(()'))
print(is_coorect('(()}'))
print(is_coorect('[()}'))
print(is_coorect('<(>'))