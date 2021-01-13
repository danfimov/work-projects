s = input()
result = ''
for elem in s:
    if elem == 'а':
        result += 'б'
    elif elem == 'б':
        result += 'а'
    elif elem == 'А':
        result += 'Б'
    elif elem == 'Б':
        result += 'А'
    else:
        result += elem
print(result)
