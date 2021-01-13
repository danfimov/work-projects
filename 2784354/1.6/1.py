first_element, difference, number_of_elements = map(int, input().split())
a = [first_element + difference*i for i in range(number_of_elements)]
print(*a)