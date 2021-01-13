a = list(map(int, input().split()))
for i in range(4):
    a = [a[-1]] + a[0:len(a)-1]
print(*a)