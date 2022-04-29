import re

class PlayingField:
    basic_field = '0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n'

    def __init__(self):
        self.current_field = PlayingField.basic_field

    @classmethod
    def replace_field(cls, field):
        cls.current_field = field

    def draw_cell(self, point, Oo):
        self.current_field = self.current_field.replace(point, Oo)
        self.replace_field(self.current_field)
        return self.current_field

game_continue = True
counter = 0
player_turn = 1
xo = 'X'

winning_combinations = [
    r'X . X . X\s. . . . .\s. . . . .\s', #Крестик в строчку
    r'. . . . .\sX . X . X\s. . . . .\s',
    r'. . . . .\s. . . . .\sX . X . X\s',
    r'X . . . .\sX . . . .\sX . . . .\s', #Крестик в столбик
    r'. . X . .\s. . X . .\s. . X . .\s',
    r'. . . . X\s. . . . X\s. . . . X\s',
    r'X . . . .\s. . X . .\s. . . . X\s', #Крестик по диагонали
    r'. . . . X\s. . X . .\sX . . . .\s',

    r'O . O . O\s. . . . .\s. . . . .\s', #Нолик в строчку
    r'. . . . .\sO . O . O\s. . . . .\s',
    r'. . . . .\s. . . . .\sO . O . O\s',
    r'O . . . .\sO . . . .\sO . . . .\s', #Нолик в столбик
    r'. . O . .\s. . O . .\s. . O . .\s',
    r'. . . . O\s. . . . O\s. . . . O\s',
    r'O . . . .\s. . O . .\s. . . . O\s', #Нолик по диагонали
    r'. . . . O\s. . O . .\sO . . . .\s',
]

#Проверка значений
def checking_values(value, reference):
    return False if value not in reference else True

#Проверка выигрыша
def check_win(pattern, check_field):
    for combination in pattern:
        combination = re.fullmatch(combination, check_field)
        if combination != None:
            return True


#Переключатель Крестик/нолик
def switch_xo(player_turn):
    return 'X' if player_turn == 1 else 'O'

#Переключатель очереди игроков
def switch_player_turn(player_turn):
    return 1 if player_turn == 2 else 2

#Ввод игрока
def player_enter():

    while True:
        print(f'Ходит {player_turn} игрок')
        player_field = str(input(f'{player_turn} игрок: куда поставим {xo}? '))
        if checking_values(player_field, field.current_field):
            return player_field
        else:
            print('Вы можете выбрать только незанятые клетки от 0 до 8!\n')
            continue


field = PlayingField()


while game_continue == True:
    print(field.current_field)
    choosen_field = player_enter()
    check_field = field.draw_cell(choosen_field, xo)

    if counter > 3:
        if check_win(winning_combinations, check_field):
            print(f'\nПобедил {xo}!')
            game_continue = False

    player_turn = switch_player_turn(player_turn)
    xo = switch_xo(player_turn)
    counter += 1
