a = list(map(int, input().split()))
minimums = []
for elem in a:
    if elem not in minimums:
        if len(minimums) < 3:
            minimums.append(elem)

            if len(minimums) == 3:  # один раз упорядочим массив минимумов
                if minimums[1] < minimums[0]:
                    minimums[1], minimums[0] = minimums[0], minimums[1]
                if minimums[2] < minimums[1]:
                    minimums[2], minimums[1] = minimums[1], minimums[2]
                if minimums[1] < minimums[0]:
                    minimums[1], minimums[0] = minimums[0], minimums[1]

        # сохраняем упорядоченность минимумов засчет постановки элемента в нужное место
        elif elem < minimums[0]:
            minimums.insert(0, elem)
            minimums.pop()
        elif elem < minimums[1]:
            minimums.insert(1, elem)
            minimums.pop()
        elif elem < minimums[2]:
            minimums[2] = elem
print(*minimums)
