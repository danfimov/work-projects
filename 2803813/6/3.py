# https://codecamp.ru/blog/python-processes-and-threads/

import numpy as np
import time
import multiprocessing as mp


def simple_matrix():
    n = 5000
    r = np.zeros((n, n))

    q = np.random.sample(n)
    p = np.random.sample(n)

    for i in range(n):
        for j in range(n):
            r[i, j] = 1 / (1 + (q[i] - p[i]) ** 2)



start_time = time.time()
simple_matrix()
print('Без использования многопоточности:', end='  ')
print(time.time() - start_time)


start_time = time.time()
processes = [mp.Process(target=simple_matrix) for _ in range(5)]
for p in processes:
    p.start()
for p in processes:
    p.join()
print('\nС использованием многопоточности:', end='  ')
print(time.time() - start_time)