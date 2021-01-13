a = [0, 1]
for i in range(98):
    a.append(a[-1] + a[-2])
print(*a)