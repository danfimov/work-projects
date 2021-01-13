def isqrt(a):
    x = a
    while True:
        x1 = (x * x + a) // (2 * x)
        if x1 >= x: return x
        x = x1


print(isqrt(16))  # есть целочисленный корень
print(isqrt(17))  # нет целочисленного корня

print(isqrt(16.))  # есть целочисленный корень - вернется  число типа float
print(isqrt(17.))  # нет целочисленного корня - вернется  число типа float