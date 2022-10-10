# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3.
#    Игрок - игрок, без бота.
# "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')   # may be string formatting is useful?

def tictactoe_game():
    player = 'X'
    rules = """Игра Крестики-нолики: для двух игроков последовательно ставящих
на поле X для первого или O для второго игрока
Выигрывает игрок первым составивший три своих знака по прямой или диагонали
Игра заканчиватеся когда заполнены все поля.
Если все поля заполнены а выигравшего нет присуждается ничья.
Первый ход за игроком X"""

    winning_moves = [[0, 1, 2],                # [0, 1, 2]
                    [3, 4, 5],                 # [3, 4, 5]
                    [6, 7, 8],                 # [6, 7, 8]
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]      # diagonals

    board_di = [0, 0, 0,                       # digital(int) representation of player moves
                0, 0, 0,
                0, 0, 0]

    possible_moves = [1 for _ in range(9)]  # [1, 1, 1,
    #   1, 1, 1,
    #   1, 1, 1]
    # possible_moves[0] = 0

    tic_tac_toe_board = [[' \u00b9', ' │ ', ' \u00b2', ' │ ', ' \u00b3'],
            ['──', '─┼─', '──', '─┼─', '───'],
            [' \u2074', ' │ ', ' \u2075', ' │ ', ' \u2076'],
            ['──', '─┼─', '──', '─┼─', '───'],
            [' \u2077', ' │ ', ' \u2078', ' │ ', ' \u2079']]
            #  ['  ', ' │ ', '  ', ' │ ', ' ']]

    pos_dict = {0: [0, 0, '¹'], 1: [0, 2, '²'], 2: [0, 4, '³'],
                3: [2, 0, '⁴'], 4: [2, 2, '⁵'], 5: [2, 4, '⁶'],
                6: [4, 0, '⁷'], 7: [4, 2, '⁸'], 8: [4, 4, '⁹']
                }

    def is_there_a_winner():
        for lines in winning_moves:
            if board_di[lines[0]] + board_di[lines[1]] + board_di[lines[2]] == 30:
                return 'X'
            elif board_di[lines[0]] + board_di[lines[1]] + board_di[lines[2]] == 3:
                return 'O'
        return False

    def print_tic_tac_board():
        temp = ''
        for v in tic_tac_toe_board:
            temp += ''.join(v) + '\n'
        print(temp)

    def change_player():
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def enter_position(p: int):
        t = pos_dict[p]
        tic_tac_toe_board[t[0]][t[1]] = tic_tac_toe_board[t[0]][t[1]].replace(t[2], player)
        if player == 'X':
            board_di[p] = 10
        else:
            board_di[p] = 1


    print(rules)
    playing = True
    while playing:
        print(is_there_a_winner())
        print(possible_moves)
        print(sum(possible_moves))

        print_tic_tac_board()
        print(f'Ход игрока  {player}  ', end='')
        pos = input(f'Введите номер позиции: ')
        if pos.isdecimal():
            if int(pos) > 0 and int(pos) < 10 :
                pos = int(pos)-1
                if possible_moves[pos]:
                    possible_moves[pos] = 0
                    enter_position(pos)
                    if is_there_a_winner() or sum(possible_moves)==0:
                        playing = False
                    else:
                        player = change_player()
                else:
                    print('Позиция уже занята! Будьте внимательнее!')
                    
            else:
                print('Некорректный ввод! Будьте внимательнее!')
                
        else:
            print('Некорректный ввод! Будьте внимательнее!')
            
    print_tic_tac_board()
    winner = is_there_a_winner()
    if winner:
        print(f'Поздравляем {winner} вы победили!')
    else:
        print(f'Поздравляем! Боевая ничья!')


tictactoe_game()
