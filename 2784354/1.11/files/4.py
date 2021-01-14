f = open('1.5.txt', 'r')

for line in f:
    surname, name, points = line.split()
    points = int(points)
    if points > 80:
        print(f'{surname} {name}')
f.close()