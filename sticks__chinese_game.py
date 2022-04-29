""" import time

#Объявляем поочередно все игровые функции

game_continue = True
game_invalid_input = False
num = 1

def printing_error():
    print('\nНекорректный ввод! Попробуй еще раз.')
    time.sleep(1)

#Проверяет корректность ввода
def checking_values(value, reference):
    if value not in reference:
        return False
    else:
        return True

#Какой игрок делает ход
def player_num(num):
    while game_continue==True:
            if num%2!=0:
                return 'первый'
            if num%2==0:
                return 'второй'

#Ввод игрока. Возвращает количество взятых палочек
def player_enter(num):
    player_1or2 = player_num(num)
    print(f'Ходит {player_1or2} игрок')
    taken_sticks = int(input(f'{player_1or2.capitalize()} игрок: сколько палочек хочешь взять? (от 1 до 3) '))
    return taken_sticks

#Выполнение хода
def step(sticks):
    print(f'\nСейчас в наличии {sticks}')
    taken_sticks = player_enter(num)
    global game_invalid_input
    if checking_values(taken_sticks, [1,2,3])==False or taken_sticks>sticks:
        printing_error()
        game_invalid_input = True
        return sticks
    else:
        game_invalid_input = False
        return sticks-taken_sticks


while game_continue==True:
    sticks = int(input('\nДревняя китайская игра в палочки.\nМожно играть с 10 или 20 палочками, что выбираешь? (10/20) '))

    if checking_values(sticks, [10,20])==False:
        printing_error()
        continue
    else:
        while sticks>0:
            sticks = step(sticks)
            if game_invalid_input==False:
                num+=1
            else:
                continue
        else:
            player_1or2 = player_num(num)
            print(f'\nПобедил {player_1or2} игрок!')
            time.sleep(1)
            game_continue = False """

sticks = 10
player_turn = 1

def can_take(sticks):
    return sticks>=1 and sticks<=3

def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2

def endgame(sticks):
    return sticks<=0

def is_more_sticks(taken, sticks):
    return taken>sticks

while (not endgame(sticks)):
    print(f'Player {player_turn} turn')
    print(f'Remaining {sticks} sticks')
    taken = (int(input(f'How many sticks you take? ')))

    if taken<1 or taken>3:
        print(f'\nYou cannot take {taken} sticks! Allowed to take 1,2,3 sticks.')
        continue

    if is_more_sticks(taken, sticks):
        print(f'\nThere are not so many sticks here! Remaining {sticks} sticks.')
        continue

    sticks-=taken
    print(f'Sticks taken {taken}\n')

    player_turn = switch_player_turn(player_turn)

    if sticks<=0:
        print(f'No more sticks in the game!\nPlayer {player_turn} wins!')