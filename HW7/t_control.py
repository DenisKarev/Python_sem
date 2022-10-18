from t_in_out import t_db_init, t_menu_inp, t_show_nums, t_input_new, t_import_f, t_export_csv, t_export_json
from t_menu import m10, m2, m3, m4, m_que, m_exp, m_empty, m_db_ne, m_fnf


def t_menu(m: int) -> int:
    if m == 11:
        if t_db_init() == -1:
            print(m_db_ne)
        m = 10
    elif m == 10:
        print(m10, end='')
        m = t_menu_inp('01234', m_que)
    elif m == 1:
        m = t_show_nums()
        if m == -1:
            print(m_empty)
            m = 10
    elif m == 2:
        print(m2, end='')
        m = t_input_new()
    elif m == 3:
        print(m3, end='')
        inp = input()
        if not inp:
            print('Ничего не введено!')
        else:
            # проверка ввода?
            m = t_import_f(inp)
            if m == -1:
                print(m_fnf)
                m = 10
    elif m == 4:
        print(m4)
        m = t_menu_inp('012', m_que)
        print(m_exp, end='')
        if m == 1:
            file = input() + '.csv'
            t_export_csv(file)
        elif m == 2:
            file = input() + '.json'
            t_export_json(file)
        else:
            m = 10
    elif m == 0:
        pass
    return m
