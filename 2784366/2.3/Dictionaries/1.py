def dictionary(file_name):
    f = open(file_name, 'r')
    result = dict()
    for line in f:
        for elem in line.split():
            if elem in result:
                result[elem] += 1
            else:
                result[elem] = 1
    return result

def preporation():
    f = open('2.3.1.txt', 'w')
    text = []
    s = input()
    while s:
        text.append(s)
        s = input()
    for string in text:
        print(string, file = f)
    f.close()

# если нужно подготовить файл - раскомментируйте
# preporation()

print(dictionary('2.3.1.txt'))