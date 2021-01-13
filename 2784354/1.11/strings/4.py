import itertools


def condition(string):
    vowel = 'ауоиэыяюеё'
    for i in range(1, len(string)):
        if (string[i] in vowel) and (string[i - 1] in vowel):
            return False
    return True


k = int(input())
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
words = [elem for elem in list(map(''.join, itertools.product(alphabet, repeat=k))) if
         condition(elem)]
print(f'Количество слов: {len(words)}')
print(*words)
