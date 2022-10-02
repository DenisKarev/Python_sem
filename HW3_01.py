# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях
# (не индексах).
# in 5
# out [10, 2, 3, 8, 9]
# 22
# in 4
# out [4, 2, 4, 9]
# 8
from random import sample

n = int(input('Enter number: '))
li = sample(range(1, n*2), n)
print(li)

def sum_odd_pos(l):
    sum = 0
    for i in range(0, len(l), 2):
        sum += l[i]
    return sum

print(sum_odd_pos(li))