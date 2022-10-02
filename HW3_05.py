# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in      8
# out     -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in      5
# out     5 -3 2 -1 1 0 1 1 2 3 5

num = 8  # int(input('Enter a number: '))

def negafibo(n):
    if n >= 1:
        li = [1, 0, 1]
        count = 1
        for i in range(1, n):
            # li.insert(i+2*i, li[count] + li[count+1])
            li.append(li[count] + li[count+1])
            # li.insert(0, li[1] - li[0])       # from previous negafibo numbers
            li.insert(0, ((-1)**i)*li[-1])      # from fibonacci number
            count += 2
    elif n == 0:
        li = [0]
    else:
        return 'Error. Wrong number.'
    return li

print(negafibo(num))