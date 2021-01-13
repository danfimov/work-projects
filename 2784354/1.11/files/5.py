f = open('1.5.txt', 'r')
result = open('1.5-result.txt', 'w')

count = 0
for line in f:
    count += 1
    surname, name, points = line.split()
    print(f'{count}) {name[0]}. {surname}', file=result)

f.close()
result.close()
