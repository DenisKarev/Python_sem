from t_control import t_menu

def t_run():
    menu = 11
    while menu:
        menu = t_menu(menu)
    else:
        print('Спасибо, до свидания!')
    return


t_run()