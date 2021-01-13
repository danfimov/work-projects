def is_prime(n):
    result = []
    steps = 0
    for number in range(2, n+1):
        is_prime = True
        for potential_divisor in range(2, number):
            steps += 1
            if number % potential_divisor == 0:
                is_prime = False
                break
        if is_prime:
            result.append(number)
    return result, steps

def is_prime_eratosthenes(N):     # n - число, до которого хотим найти простые числа 
    steps = 0
    A = [True]*(N+1)
    k = 2
    while k*k <= N:
        if A[k]:
            i = k*k
            while i <= N:
                steps += 1
                A[i] = False
                i += k
        k += 1
    return [i for i in range(2, N+1) if A[i]], steps

n = 10
print(f'Для n = {n} число шагов нашего алгоритма = {is_prime(n)[1]}; решето Эратосфена делает {is_prime_eratosthenes(n)[1]} шагов.')
n = 25
print(f'Для n = {n} число шагов нашего алгоритма = {is_prime(n)[1]}; решето Эратосфена делает {is_prime_eratosthenes(n)[1]} шагов.')
n = 50
print(f'Для n = {n} число шагов нашего алгоритма = {is_prime(n)[1]}; решето Эратосфена делает {is_prime_eratosthenes(n)[1]} шагов.')
n = 100
print(f'Для n = {n} число шагов нашего алгоритма = {is_prime(n)[1]}; решето Эратосфена делает {is_prime_eratosthenes(n)[1]} шагов.')
#  очевидно, алгоритм, использующий решето Эратосфена, работает быстрее