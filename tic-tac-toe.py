import time
import os
import sys
from IPython.display import clear_output


### GLOBAL VARIABLES AND DICTIONARIES ###

# these are for style points...
intro1 = 'Shall we play a game...?'
intro2 = 'Welcome to Tic Tac Toe!'

# used to track Player inputs (X/O) throughout the game
tictac = {
    't1':' ','t2':' ','t3':' ',
    'm1':' ','m2':' ','m3':' ',
    'b1':' ','b2':' ','b3':' '
    }

# used to display input values (1-9) as they correspond to the game board
num_pad = {
    't1':'7','t2':'8','t3':'9',
    'm1':'4','m2':'5','m3':'6',
    'b1':'1','b2':'2','b3':'3'
    }

# used to convert number values from 'display_board' into symbol values on 'tictac'
translator = {
    '7':'t1','8':'t2','9':'t3',
    '4':'m1','5':'m2','6':'m3',
    '1':'b1','2':'b2','3':'b3'
    }

# used to record Player symbol assignments and to coordinate game logic
players = {
    'player':['PLAYER_1','PLAYER_2'],
    'symbol':['','']
    }

# used to track turns between player moves
player_idx = 0

# rather than check for a full game board, this value stops the game after 9 turns
move_ct = 0

# handles the outer game_on loop to start the game from play_again() --> reset()
game_on = True

def dramatic_print(intro,delay):
    for i in intro:
        print(i, end = '', flush=True)
        time.sleep(delay)
    print()


def clear_screen():
    if 'ipykernel' in sys.modules:
        # specifically for Jupyter Notebooks...
        clear_output()
    else:
        os.system('clear')


def game_board(tictac):
    print(
    f" {tictac['t1']} | {tictac['t2']} | {tictac['t3']} \n"
    "-----------\n"
    f" {tictac['m1']} | {tictac['m2']} | {tictac['m3']} \n"
    "-----------\n"
    f" {tictac['b1']} | {tictac['b2']} | {tictac['b3']} "
    )


def player_symbol(player_idx):
    choose_ur_char = ['X','x','O','o']
    allowable = False

    while allowable == False:
        players['symbol'][player_idx] = input(f"{players['player'][player_idx]}, which symbol would you like to use (enter X/x or O/o)? ")
        if players['symbol'][player_idx].isascii():
            if players['symbol'][player_idx] in choose_ur_char:
                allowable = True
            else:
                print('Please enter either X/x or O/o...')
                allowable = False
    players['symbol'][player_idx] = players['symbol'][player_idx].upper()

    if players['symbol'][player_idx] == 'X':
        players['symbol'][(player_idx + 1) %2] = 'O'
    else:
        players['symbol'][(player_idx + 1) %2] = 'X'

    print('Symbols have been chosen!')
    print(f"{players['player'][player_idx]}: {players['symbol'][player_idx]}")
    print(f"{players['player'][(player_idx + 1) %2]}: {players['symbol'][(player_idx + 1) %2]}")
    time.sleep(2.5)


def player_move(player_idx):
    move = ' '
    clear_screen()
    game_board(num_pad)
    print('\n     |')
    print('     |')
    print(r'    \|/''\n')
    game_board(tictac)
    
    while True:
        move = input(f"{players['player'][player_idx]}! Pick an available spot on the board using the corresponding numbers (1-9): ")
        if not move.isdigit():
            print('Sorry, that\'s not a number...')
        elif move not in num_pad.values():
            print('You must pick a number between 1 and 9...')
        else:
            return str(move)


def board_position(player_idx):
    pos = translator[move]

    try:
        if tictac[pos] == ' ':
            tictac[pos] = players['symbol'][player_idx]
            clear_screen()
            game_board(tictac)
            return True
        else:
            print("Invalid move; try again!")
            time.sleep(2)
            return False
    except KeyError:
            print('Invalid board position.')
            return False


def win_condition(tictac,players,player_idx):
    
    px_name = players['player'][player_idx]
    px_sym = players['symbol'][player_idx]

    win_pos = (
        ['t1', 't2', 't3'],
        ['m1', 'm2', 'm3'],
        ['b1', 'b2', 'b3'],
        ['t1', 'm1', 'b1'],
        ['t2', 'm2', 'b2'],
        ['t3', 'm3', 'b3'],
        ['t1', 'm2', 'b3'],
        ['t3', 'm2', 'b1']
    )

    for con in win_pos:
        if all(tictac[pos] == px_sym for pos in con):
            clear_screen()
            game_board(tictac)
            print(f"{px_name} wins!!!")
            return True
    return False


def reset():
    global move_ct, tictac, player_idx, game_on

    move_ct = 0
    clear_screen()
    tictac = {key: ' ' for key in tictac}
    player_idx = (player_idx + 1) %2
    print(f'{players['player'][player_idx]} goes first, this time!')
    time.sleep(2)
    game_on = True
    tic_tac_toe()


def play_again():
    global game_on

    yes = ['Yes','yes','Y','y']
    no = ['No','no','N','n']
    replay = ''
    correct_response = False

    while replay.isascii() == False or correct_response == False:
        replay = input('Would you like to play again ([y]es, [n]o)? ')
        if replay.isascii() == False:
            print('Sorry, that\'s not a word/letter...')
        if replay.isascii():
            if replay in yes or no:
                correct_response = True
            else:
                print('You must answer, "[y]es, [n]o."')
                correct_response = False
    
    if replay in yes:
        print('Let\'s do it!\nOne moment...')
        time.sleep(3)
        return True
    elif replay in no:
        print('Hope you had fun! Until next time...')
        time.sleep(1.5)
        return False


def tic_tac_toe():
    global game_on, move_ct, player_idx, move

    while game_on:
        clear_screen()
        player_symbol(player_idx)

        while move_ct < 9:
            move = player_move(player_idx)

            while True:
                if board_position(player_idx):
                    break
                else:
                    move = player_move(player_idx)

            if win_condition(tictac, players, player_idx):
                game_on = play_again()
                if not game_on:
                    break
                else:
                    reset()
                    break

            else:
                move_ct += 1
                player_idx = (player_idx + 1) % 2

        if move_ct == 9:
            print('BUST! It\'s a draw!')
            time.sleep(2)
            game_on = play_again()
            if not game_on:
                break
            else:
                reset()
                break


## Dramatic introduction (LOL):
dramatic_print(intro1,delay=0.1)
print('.'); time.sleep(1); print('.'); time.sleep(1); print('.'); time.sleep(1)
dramatic_print(intro2,delay=0.05); time.sleep(2)
print('\n')
game_board(tictac)
print('\n')

## Game logic:
tic_tac_toe()
