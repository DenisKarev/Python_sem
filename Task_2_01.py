# 1. Напишите программу, которая принимает на вход число N и
#    выдаёт последовательность из N членов.

# n = int(input('Введите число: '))
# count = 1
# for i in range(n):
#     print(count, end=', ')
#     count *=-3

n = int(input('Введите число: '))
for i in range(n):
    print(((-3)**i), end=' ')