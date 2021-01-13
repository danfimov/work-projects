
# F0 = 0, F1 = 1, F2= 1, F3 = 2...
def fib(n):
    f_1 = 0
    f_2 = 1
    print(f_1, f_2, end=' ')
    for i in range(2, n):
        f_1, f_2 = f_2, f_1 + f_2
        print(f_2, end=' ')