# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#     Напишите программу, которая найдёт разницу между максимальным и минимальным значением
#     дробной части элементов.
# in    5
# out   [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in      3
# out     [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
from random import random

num = 5 # int(input('Enter a number: '))
li = []
for i in range(num):
    li.append(round(random()*10, 2))
print(li)

def diff_in_maxmin_fraction(l):
    for i in range(len(l)):
        l[i] = round(l[i] % 1, 2)
    max_l = max(l)
    min_l = min(l)
    print('Min: ', min_l, 'Max: ', max_l, 'Difference: ', round(max_l-min_l, 2))

diff_in_maxmin_fraction(li)