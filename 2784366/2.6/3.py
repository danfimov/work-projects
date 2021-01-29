N0, N = map(int, input("Введите начальное и конечное числа: ").split())

K = [0] * (N + 1)

K[N0] = 1
for i in range(N0 + 1, N + 1):
    K[i] = K[i - 1]
    if i % 4 == 0:
        K[i] += K[i // 4]

print("Количество программ ", K[N])
