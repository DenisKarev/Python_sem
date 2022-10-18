from genericpath import exists


def t_file_read(file: str) -> list:
    if exists(file):
        with open(file, 'r', encoding='utf-8') as data:   # , encoding='utf-8'
            ret_data = []
            for line in data.readlines():
                line = ''.join(line.replace('\n', ''))
                ret_data.append(line)
        return ret_data
    else:
        return -1


def t_file_write(file: str, data) -> list:
    with open(file, 'a', encoding='utf-8') as waf:
        for line in data:
            waf.write(line+'\n')
    return data


def t_database_read() -> list:
    if exists('t_database.csv'):
        with open('t_database.csv', 'r', encoding='utf-8') as db_r:
            ret_data = []
            for line in db_r.readlines():
                if line[0] == '\ufeff':
                    line = line[1:]
                line = ''.join(line.replace('\n', ''))
                ret_data.append(line)
        return ret_data
    else:
        with open('t_database.csv', 'w', encoding='utf-8') as db_w:
            db_w.write('\ufeff')
        return -1

def t_database_update(data: str):
    with open('t_database.csv', 'a', encoding='utf-8') as waf:
        waf.write(data + '\n')
    return
