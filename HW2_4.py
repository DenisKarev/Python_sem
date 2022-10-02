# 4. Напишите программу, которая принимает на вход 3 числа. Задайте список из N элементов,
#    заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Number of elements: 5
# Position one: 1
# Position two: 3
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

num_elems = int(input('Enter a number N: '))
n1 = int(input('Enter a position 1: '))
n2 = int(input('Enter a position 2: '))

res_str = []
if num_elems > 0:
    for i in range(-num_elems, num_elems+1):
        res_str.append(i)
else:
    for i in range(num_elems, -num_elems+1):
        res_str.append(i)

if n1 > num_elems*2+1 or n2 > num_elems*2+1:
    print('One of the positions out of range of N')
else:
    print(' -> ', res_str)
    print(' -> ', res_str[n1-1]*res_str[n2-1])