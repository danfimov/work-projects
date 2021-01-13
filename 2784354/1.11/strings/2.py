s = input()


def is_palindrom(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


'''
Для проверки:
1) арозаупаланалапуазора - да
2) казак - да
3) яаркакрая - да
'''

print('Палиндром' if is_palindrom(s) else 'Не палиндром')
