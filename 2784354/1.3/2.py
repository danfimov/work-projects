years = int(input())
if 11 <= years%100 <= 14:
    print(f'{years} лет')
elif 2 <= years%10 <= 4:
    print(f'{years} года')
elif years%10 == 1:
    print(f'{years} год')
else:
    print(f'{years} лет')