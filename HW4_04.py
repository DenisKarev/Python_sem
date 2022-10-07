# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (от 0 до 10) многочлена, записать в файл полученные многочлены не менее 3-х раз.
# in 9 5 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in 0 -1 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
from random import choice, randint


def get_polynom(n: int):
    factors = [randint(0, 9) for _ in range(n + 1)]
    print(factors)
    res = ''
    for i in range(len(factors)-1, 0, -1):
        if factors[i]:
            res += (f'{factors[i]}*x^{i} {choice("+-")} ')
    res += (f'{factors[0]} = 0')
    print(res)
    return res


with open('hw4_4out2.txt', 'a', encoding='utf-8') as file:
    for i in range(3):
        nli = get_polynom(int(input('Enter the K number: ')))
        file.write(f'{nli}\n')
