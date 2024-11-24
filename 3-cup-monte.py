from random import shuffle

og_list = [' ', 'O', ' ']

def shufflist(og_list):
    shuffle(og_list)
    return og_list

def player_guess():

    guess = ''

    while guess not in ['1', '2', '3']: # <-- error-handling
        guess = input('Pick a number! 1, 2, or 3: ')

    return int(guess) # <-- 'input()' always returns a str, so we convert to int here...

def check_guess(guess_list, guess):
    if guess_list[guess - 1] == 'O': # <-- code needs to refer to the index (0-2), but I ask for 1-3 for the less coding-inclined; ergo, subtraction to align w/ index
        #print(f'You guessed, {guess}...')
        print('Correct!')
    else:
        #print(f'You guessed, {guess}...')
        print('Wrong guess!')
        print(guess_list)

guess_list = shufflist(og_list)
guess = player_guess()
check_guess(guess_list, guess)