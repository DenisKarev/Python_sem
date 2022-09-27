# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
#
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

num = int(input('Enter a number: '))
res_str = []
for i in range(1, num+1):
    res = 1
    for j in range(1, i+1):
        res *= j
    res_str.append(res)
print(res_str)