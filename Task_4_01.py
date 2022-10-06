# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

str_nums = '*2 -101 200* 100.' # input('Enter numbers: ')
# VARiant I
# list_l = [int(x.strip(',*.;:')) for x in str_nums.split() if x.replace('-','').isdigit()]
# list_l = [x.strip(',*.;:') for x in str_nums.split() if x.replace('-','').isdigit()]
# print(f'Min: {min(list_l, key=int)}')
# print(f'Max: {max(list_l, key=int)}')

# VARiant II
list_2 = []
for x in str_nums.split():
    if x.strip(',*.;:').replace('-','').isdigit():
        list_2.append(x.strip(',*.;:'))

print(list_2)
print(f'Min: {min(list_2, key=int)}')   # min in string list becouse of key
print(f'Max: {max(list_2, key=int)}')   # max in string list becouse of key


# VARiant III
# def check(str_list):
#     for i, num in enumerate(str_list):
#         str_list[i] = num.strip('.,;:?!')
#         if not str_list[i].replace("-", "").isdigit():
#             return []
#     return str_list

# def find_max_min(nums_str: str):
#     list_nums = nums_str.split()
#     right_list = check(list_nums)

#     if right_list:
#         return min(right_list, key=int), max(right_list, key=int)
#     print("The data is incorrect")
#     return []

# print(*find_max_min(input("Enter the numbers separated by a space: ")))