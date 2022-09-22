# 1. Напишите программу, которая принимает на вход два числа
#    и проверяет, является ли одно число квадратом другого.

a = int(input('Enter number 1:'))
b = int(input('Enter number 2:'))

if a**2 == b or b**2 == a:
    print('yes')
else:
    print('no') 