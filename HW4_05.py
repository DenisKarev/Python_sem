# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
#  Задача - сформировать файл, содержащий сумму многочленов.

def sum_polys(f1: str, f2: str):
    with open(f1, 'r', encoding='utf-8') as fin1,\
         open(f2, 'r', encoding='utf-8') as fin2:
        data1 = fin1.readlines()
        data2 = fin2.readlines()
        print(data1)
        print(data2)
        if len(data1) == len(data2):
            file3 = 'hw4_5out.txt'
            with open(file3, 'a', encoding='utf-8') as outfile:
                for i in range(len(data1)):
                    print(f'{data1[i][:-5]} + {data2[i]}', end = '')
                    outfile.write(f'{data1[i][:-5]} + {data2[i]}')  # без enumerate
        else:
            print('Can\'t sum polynoms ;((')

path1 = 'hw4_4out1.txt' # input('Enter file name: ')
path2 = 'hw4_4out2.txt'
sum_polys(path1, path2)