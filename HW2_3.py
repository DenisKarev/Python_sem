# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n
#    и выведите на экран их сумму.
#    Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input('Enter a number: '))
res_str = []
sum = 0
for i in range(1, num+1):
    res_str.append(round((1+(1/i))**i))
    sum += res_str[i-1]
print(res_str,' ->', sum)