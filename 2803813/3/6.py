def crossing(*params):
    if len(params) == 0:
        return set()
    if len(params) == 1:
        return set(params[0])

    result = set(params[0])
    for i in range(1, len(params)):
        if list != type(params[i]):
            raise TypeError('Передан не список')
        result = result.intersection(set(params[i]))
    return result

print(crossing([1,2,3], [2,3]))