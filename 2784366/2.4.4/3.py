from tree import *

s = input("Введите арифметическое выражение без скобок: \n")
T = makeTree(s)
print("Результат:", calcTree(T))
print('\nОбход в ширину: ', end='')
tree_width_traversal(T)