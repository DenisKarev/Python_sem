# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.


a = float(input('Enter number:'))
new = a*10

if a % 10 == 0:
    print('No')
else:
    print(int(a*10%10))

# n =float(input('Введите число'))
# new_n=n*10
# a=int(new_n%10)
# if a!=0:
#     print (a)
# else:
#     print('no')
