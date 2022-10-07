# 2. Дан список чисел. Создайте список, в который попадают числа,
#    описываемые возрастающую последовательность.
#    Порядок элементов менять нельзя.
# [10, 0, 5, 11, 6, 1, 15, 10]
# in [19, 5, 1, 14, 5, 9, 15, 11, 12, 2]

from random import choices


def gen_list(size: int):
    new_list = choices(range(1, size * 2), k=size)
    return new_list


def gen_progressions(li: list):
    res_list = []
    for i in range(len(li)):
        comp = li[i]
        lis1 =[comp]
        for j in range(i + 1, len(li)):
            if li[j] > comp:
                comp = li[j]
                lis1.append(comp)
        if len(lis1) > 1:
            res_list.append(lis1)
    return res_list


nl = gen_list(10)
print(nl)
print(gen_progressions(nl))