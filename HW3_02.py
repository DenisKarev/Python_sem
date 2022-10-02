# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4
# out [2, 5, 8, 10]
# [20, 40]
from random import sample
n = 4 #int(input('Enter number: '))
li = sample(range(1, n*2), n)
print(li)

def mult_paired_elems(l):
    new_l = []
    for i in range(0, len(l)//2):
        new_l.append(l[i] * l[-i-1])
    if len(l) % 2:
        new_l.append(l[len(l)//2])
    return new_l

print(mult_paired_elems(li))