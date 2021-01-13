
while True:
    try:
        n = int(input())
        break
    except:
        print('Некорректное число, введите новое')
        continue


for number in range(1,n+1):
    if number == (number * number) % (10**len(str(number))):
        print(number)