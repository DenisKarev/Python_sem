from t_file import t_database_read, t_database_update, t_file_read, t_file_write

t_data = []
t_type = {'0':'неопределен', '1':'Домашний', '2':'Мобильный', '3': 'Рабочий', '4': 'Основной'}

def t_db_init():
    global t_data
    t_data = t_database_read()
    if t_data == -1:
        t_data = []
        return -1
    return

def t_menu_inp(val: str, que: str) -> int:
    """
    val = '012' возможные значения ввода \n
    que = 'Введите пункт меню: ' строка запроса ввода\n
    возвращает пункт выбранного меню -> int
    """
    res = ' '
    while res not in val:
        res = input(que)
        if not res:
            res = ' '
    else:
        return int(res)


def t_input_new():
    global t_data
    res_line = f'{len(t_data)},'
    inp = input()
    if not inp:
        print('Ничего не введено!')
    else:
        # проверка ввода?
        res_line += inp
        t_data.append(res_line)
        t_database_update(res_line)
    return 1


def t_import_f(fname: str):
        global t_data

        data = t_file_read(fname)
        if data == -1:
            return -1
        else:
            for line in data:
                res_line = f'{len(t_data)},'
                if line == '':
                    continue
                elif line[0] == '\ufeff':
                    line = line[1:]
                res_line += line
                t_data.append(res_line)
                t_database_update(res_line)
        return 1


def t_export_csv(fname: str):
    global t_data
    res_list = []
    for line in t_data:
        temp = [x for x in line.split(',')]
        na, fa, ot, numt, typ = temp[1:6]
        res_list.append(f'{na},{fa},{ot},{numt},{t_type[typ]},')
    t_file_write(fname, res_list)
    return

def t_export_json(fname: str):
    global t_data
    
    return

def t_show_nums():
    global t_data
    if len(t_data) > 1:
        print(f"{'id':4} {'Фамилия':15} {'Имя':15} {'Отчество':18} {'Номер телефона':20} {'Тип':8}")
        for line in t_data:
            temp = [x for x in line.split(',')]
            if len(temp) < 6:
                pass
            else:
                id, na, fa, ot, numt, typ = temp[:6]
                print(f'{id:4} {na:15} {fa:15} {ot:15} {numt:20} {t_type[typ]:8}')
        return 10
    # elif len(t_data) == 1:
    #     return -1
    else:
        return -1
