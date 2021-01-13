def dictionary(file_name):
    f = open(file_name, 'r')
    result = dict()
    for line in f:
        for elem in line.split():
            if not elem[-1].isalpha():
                elem = elem[:len(elem) - 1]

            if elem in result:
                result[elem] += 1
            else:
                result[elem] = 1
    return sorted([key for key in result.keys()], key=lambda x: result[x], reverse=True)


def preporation():
    f = open('2.3.1.txt', 'w')
    text = []
    s = input()
    while s:
        text.append(s)
        s = input()
    for string in text:
        print(string, file=f)
    f.close()


# если нужно подготовить файл - раскомментируйте
# preporation()

print(dictionary('2.3.1.txt'))