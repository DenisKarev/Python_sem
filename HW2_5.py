# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10 elements?
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

num_elems = 10 # int(input('Enter a number of elements, N: '))

res_str = []
for i in range(num_elems):
    res_str.append(i)
print(' -> ', res_str)
for i in range(num_elems):
    t_index = randrange(num_elems)
    temp = res_str[i]
    res_str[i] = res_str[t_index]
    res_str[t_index] = temp
print(' -> ', res_str)
