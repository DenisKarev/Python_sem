# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без использования встроенной функции преобразования, без строк.
# in      88
# out     1011000
# in      11
# out     1011

num = int(input('Enter a number: '))

def conv2bin(n):
    if not n: return 0
    aka_bin_l = []
    aka_bin = 0
    while n:
        aka_bin_l.append(n % 2)
        n //= 2
    for i in range(len(aka_bin_l)):
        aka_bin += aka_bin_l[i] * 10**i
    return aka_bin

print(conv2bin(num))