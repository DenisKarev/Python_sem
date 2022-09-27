# 1. Напишите программу, которая принимает на вход вещественное число
#    и показывает сумму его цифр.
#    in -> out
#  - 6782 -> 23
#  - 0.67 -> 13
#  - 198.45 -> 27

num = float(input('Enter a floating point number: '))
print(num, end=' ')

# while round(num % 1, 8) > 0:
#     num *= 10
# num = int(num)

size = len(str(num))-1
for i in range(size):
    num *= 10
sum = 0
num = int(num)
while num > 0:
    sum += num % 10
    num //= 10
print(sum)