# 1. Вычислить число c заданной точностью d
# in      Enter a real number: 9
#         Enter the required accuracy '0.0001': 0.000001
# out     9.000000
# in      Enter a real number: 8.98785
#         Enter the required accuracy '0.0001': 0.001
# out     8.988
from decimal import *

# def get_precision(pr: str):
#     pr = pr.split('.')[1]
#     count = 1
#     if pr[-1] == '1':
#         if '0' in pr:
#             zer = pr.count('0')
#             zer += 1
#             if len(pr) == zer:
#                 return zer
#             else:
#                 return 0
#         else:
#             return 0
#     else:
#         print('Error. Please enter accuracy like in example.')
#         return 0
#     print("What?")
#     return count

def get_precision(pr: str):
    res = -1
    if pr[1] !='.' or pr[-1] !='1' or pr.count('0') < len(pr)-2 or pr.count('1') > 1:
        breakpoint
    else:
        res = len(pr)-2 # or pr.count('0')
    return res

dec = Decimal(9.00112233445566778899)  # Decimal(input('Enter a real number: '))
# dec = int(input('Enter a real number: '))
prec = '0.00000000000000001'  # input("Enter the required accuracy '0.0001': ")
# print(getcontext())

accu = get_precision(prec)
if accu == -1:
    print('Wrong input. Please enter accuracy like in example -> 0.0001')
else:
    print(f'Selected accuracy: {accu} digits after the dot')
    # print(f'String:  {str(dec)}')
    # print(f'Decimal: {Decimal(dec)}')
    print(f'Round Decimal: {round(Decimal(dec), accu)}')
    print(f'f string float {dec:.{accu}f}')
    print(f'Decimal.quanti {Decimal(dec).quantize(Decimal(prec))}')