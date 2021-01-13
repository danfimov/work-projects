def is_coorect(string):
    stack = []
    for elem in string:
        if elem in '(<[{':
            stack.append(elem)
        else:
            if len(stack) != 0:
                pair = stack[-1]
                scobki = pair + elem
                if scobki == '()' or scobki == '{}' or scobki == '[]' or scobki == '<>':
                    stack.pop()
            else:
                return False
    return not stack

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