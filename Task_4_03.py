# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.
# in 11 17
# out 187
# in 11 17
# out 187

from math import gcd
a = int(input('Enter a number:'))
b = int(input('Enter a number:'))

print(a*b//gcd(a,b))
print(gcd(a,b))