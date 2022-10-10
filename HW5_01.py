# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#    В тексте используется разделитель пробел.
# in    Number of words: 10
# out   авб абв бав абв вба бав вба абв абв абв
#       авб бав вба бав вба
# in    Number of words: 6
#       out ваб вба абв ваб бва абв
#       ваб вба ваб бва
# in    Number of words: -1
# out   The data is incorrect
from random import sample

# li1 = 'абв авб абв бав абв вба бав вба абв абв абв'

def gen_list_words(num: int):
    if num > 0:
        reslist = [''.join(sample('абв', k=3)) for _ in range(num)]
    else:
        reslist = []
    return reslist

li1 = gen_list_words(int(input('Enter a number of words: ')))
if li1:
    li2 = [li1[x] for x in range(len(li1)) if li1[x] != 'абв']
    print(li1)
    print(li2)
else:
    print('Incorrect input!')
