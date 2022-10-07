# 2. Задайте натуральное число N. Напишите программу,
#    которая составит список простых множителей числа N.
# in      54
# out     [2, 3, 3, 3]
# in      9990
# out     [2, 3, 3, 3, 5, 37]
# in      650
# out     [2, 5, 5, 13]

def simple_divs(nu: int):
    res = []
    i = 2
    n = nu
    while i <= nu:
        if n % i ==0:
            res.append(i)
            n //= i
        if n % i:
            if i == 2: i+=1
            else: i+=2
    return res

num = 9990 # int(input('Enter a number N: '))
# 5140 15140 5401
print(num,' ->',simple_divs(num))