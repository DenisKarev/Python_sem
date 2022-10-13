# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
#    значения которых больше предыдущего элемента. Use comprehension.
# in        9
# out       [15, 16, 2, 3, 1, 7, 5, 4, 10]
#           [16, 3, 7, 10]
# in        10
# out       [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
#           [24, 15, 23, 25]
from random import sample

n = 9 # int(input('Enter a number of elements in the list: '))
li = sample([i for i in range(1, n*2)], n)                             # random list generation
li_greater = [li[i] for i in range(1, len(li)) if li[i] > li[i-1]]     # list [n] > [n-1] in random list
print(li)
print(li_greater)