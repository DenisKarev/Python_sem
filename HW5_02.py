# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.
# in    Enter the name of the file with the text: 'text_words.txt'
#       Enter the file name to record: 'text_code_words.txt'
#       Enter the name of the file to decode: 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a
# 1v2b2w2P3u2T1Y1y2W2Q


def pack_rle(dat: str):
    templist = dat.splitlines()
    res = []
    for stri in templist:
        stri += ' '
        char = stri[0]
        count = 0
        resstr = ''
        for ch in stri:
            if char == ch:
                count += 1
            else:
                resstr += (f'{count}{char}')
                char = ch
                count = 1
        res.append(resstr)
    return res

def unpack_rle(dat: str):
    templist = dat.splitlines()
    res = []
    count = 0
    for stri in templist:
        resstr = ''
        count = ''
        for ch in stri:
            if ch.isdecimal():
                count += ch
            else:
                resstr += ch * int(count)
                count = ''
        res.append(resstr)
    return res

def write_list(path_file: str, li: list):
    with open(path_file, 'w', encoding='utf-8') as wfile:
        for dat in li:
            wfile.write(dat + '\n')

def read_list(path_file: str):
    with open(path_file, 'r', encoding='utf-8') as rfile:
        dat = [line for line in rfile]
    return dat

work_list = ['aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa', 'vbbwwPPuuuTTYyWWQQ']
# work_str = 'aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa','vbbwwPPuuuTTYyWWQQ'
file4in = 'file4in.txt'  # input('Enter the filename with text: ')
# input('Enter the filename to write RLE-packed output and then decode?: ')
fileout = 'fileout.txt'
filedec = 'fileout.txt'  # input('Enter the filename to decode RLE-packed: ')

write_list(file4in, work_list)

data = ''.join(read_list(file4in))
print('Data: ->', data)

data_rle = pack_rle(data)
write_list(fileout, data_rle)

data_packed = ''.join(read_list(filedec))
data_unp = unpack_rle(data_packed)

print('Packed data   ->', data_packed)
# print('work_list -> ', work_list)
print('Data unpacked -> ', data_unp)
