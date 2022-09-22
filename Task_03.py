# 3. Напишите программу, которая будет на вход принимать число N
#   и выводить числа от -N до N

a = int(input('Enter number 1:'))
# b=-a
for i in range(-a,a):
    print(i, end=' ')

# num = int(input())
# neg_num = -num

# while num != neg_num:
#     print(neg_num, end=", ")
#     if num > 0:
#         neg_num += 1
#     else:
#         neg_num -= 1
