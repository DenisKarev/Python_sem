# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.
from random import choices

def create_list(num: int, abc: str):
    n_list = []
    for i in range(num):
        a = choices(abc, k=3)
        n_list.append(''.join(a))  # ''.join(choices(words, k=3))
    return n_list

def list_search(lst, value):
    if lst.count(value) > 1:
        n = lst.index(value)
        print(lst.index(value, n+1))
    else:
        print('-1')

words = create_list(30, 'zxy')
print(words)
list_search(words, 'zzz')
exit()

from random import choices
def list_new(n, word):
    new_list =[]
    for i in range(n):
        a=choices(word,k=3)
        new_list.append(''.join(a))
    return new_list

def list_search(my_list, key):
    if my_list.count(key) >1:
        print('Yes')
        n=my_list.index(key)
        print(my_list.index(key,n+1))
    else:
        print(-1)
result=list_new(20, "abc")
print(result)
list_search(result, input())