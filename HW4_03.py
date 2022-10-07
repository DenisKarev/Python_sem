# 3. Задайте последовательность чисел. Напишите программу, которая выведет
#    список неповторяющихся элементов исходной последовательности в том же порядке.
# in      7
# out     [4, 5, 3, 3, 4, 1, 2]
#         [5, 1, 2]
# in      -1
# out     Negative value of the number of numbers!
#         []
# in      10
# out     [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#         [6, 2, 3, 0, 9]
from random import choices
def uniqs_in_list(l: list):
    res = [l[_] for _ in range(len(l)) if l.count(l[_]) <= 1]
    # for i in range(len(l)):
    #     if l.count(l[i]) <= 1:
    #         res.append(l[i])
    return res

n = 10 # int(input('Enter a number: '))
if n <= 0:
    print('Negative or zero value entered - empty list is useless )')
else:
    l_rng = 1
    h_rng = 10
    n_list = choices(range(l_rng, h_rng), k = n)

    print(n_list)
    print(uniqs_in_list(n_list))