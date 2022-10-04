# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.
#   D = b**2 - 4ac
from math import sqrt


def find_roots(a, b, c):
    if a == 0:
        return print(f'root: a==0\n')
    discr = b**2 - 4*a*c
    with open('roots.txt', 'a', encoding='utf-8') as rf:
        rf.write(f'Equation: {a}x² + {b}x + {c} = 0\n')
        if discr > 0:
            rf.write(f'root 1: {(-b + sqrt(discr)) / (2 * a)} ')
            rf.write(f'root 2:{(-b - sqrt(discr)) / (2 * a)}\n')
        elif discr == 0:
            rf.write(f'{-b / (2 * a)}')
        else:
            rf.write(f'No roots')


# int(input('Enter a number A:'))
for i in range(3):
    find_roots(int(input('Enter A:')), int(input('Enter B:')), int(input('Enter C:')))
