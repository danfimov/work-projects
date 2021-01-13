a, b = map(int, input().split())
result = 0
for i in range(abs(b)):
    result += abs(a)
if (a > 0 and b < 0) or (a < 0 and b > 0):
    result = -result
print(f'{a} * {b} = {result}')