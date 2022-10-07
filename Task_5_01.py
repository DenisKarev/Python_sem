# 1. В файле находится N натуральных чисел, записанных через пробел.
#    Среди чисел не хватает одного, чтобы выполнялось условие
#    A[i] - 1 = A[i-1]. Найдите это число.
from random import choice
num = 10 # int(input('Enter a number: '))

def gen_list(n: int):
    res = [x for x in range(n + 1)]
    res.remove(choice(res))
    return res

def find_error_inlist(l: list):
    for i in range(1, len(list1)):
        if list1[i] - 1 != list1[i-1]:
            return i
    return -1

list1 = gen_list(num)
print(list1)
n = find_error_inlist(list1)
print(n)
