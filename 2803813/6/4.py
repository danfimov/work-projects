# http://toly.github.io/blog/2014/02/13/parallelism-in-one-line/

import os
import time
from multiprocessing.dummy import Pool as ThreadPool


def find_file(files):
    for file in files:
        try:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    for line in f:
                        if line.find('key') != -1:
                            print(f.name)
                            break
        except UnicodeDecodeError:
            print('Не удалось распарсить файл')


def find_key(file):
    try:
        if file.endswith(".txt"):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                for line in f:
                    if line.find('key') != -1:
                        print(f.name)
                        break
    except UnicodeDecodeError:
        print('Не удалось распарсить файл')


start_time = time.time()
print('Результаты:')
for root, dirs, files in os.walk("/Users/mrrobot/PycharmProjects/pythonProject1"):
    find_file(files)
print('------\nБез использования многопоточности: ', time.time() - start_time, end='\n\n')

start_time = time.time()
print('Результаты:')
for root, dirs, files in os.walk("/Users/mrrobot/PycharmProjects/pythonProject1"):
    pool = ThreadPool(4)
    result = list(map(find_key, files))
    pool.close()
    pool.join()
print('------\nС использованием многопоточности: ', time.time() - start_time)

# Использование библиотеки multiprocessing не оправдано.
# Накладные расходы на поддержание многопоточности больше, чем сэкономленные ресурсы
