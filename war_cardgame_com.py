import time
from random import shuffle
from typing import List


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
                
    def shuffle(self):
        shuffle(self.all_cards)
        
    def deal_one(self):
        if not self.all_cards:
            raise ValueError('No cards left in the deck!')
        return self.all_cards.pop()


class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards: List[Card] = []
        
    def remove_one(self):
        # Index 0 will represent the "top" of the deck...
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
        if len(self.all_cards) == 1:
            return f'Player {self.name} has {len(self.all_cards)} card.'
        else:
            return f'Player {self.name} has {len(self.all_cards)} cards.'


## Player name assignment (for style points...):
def choose_ur_char():

    player_select = ['Gambit', 'Hisoka', 'Hawkins', 'Yugi', 'Kaiba', 'The Joker']

    shuffle(player_select)

    player1 = Player(player_select.pop())
    player2 = Player(player_select.pop())

    print(f'\nPlayer 1 (P1): {player1.name}')
    print(f'Player 2 (P1): {player2.name}')
    time.sleep(1.5)

    return player1, player2


## Number of cards drawn for War scenarios chosen by human spectator (3 = more iterations; 5 = shorter game)""
def card_count():

    while True:
        try:
            cc = int(input(f'Enter (3) or (5) for cards drawn during War (more cards --> shorter game): '))

            if cc not in [3, 5]:
                print('"I am neither (3) nor (5); I am the one who will perpetuate this loop!" (that\'s you...)')
            else:
                print(f'War cards set to: {cc}')
                time.sleep(1)
                return cc

        except ValueError:
            print('You must enter either three (3) or five (5)...')


## Basically determines how long you want the game to go on for, and whether you want to spectate more closely:
def round_sleep():
    print('The round number is announced at the start of each round, followed by a brief pause.')
    time.sleep(1.5)
    print('\nThese games go on for hundreds of turns...')
    time.sleep(1.5)

    while True:
        try:
            rts = float(input('Enter a value between (0) and (1) (increments of 0.05) to DETERMINE THE PAUSE LENGTH (0 == no pause): '))

            if 0 <= rts <= 1:

                if int(rts * 100) %5 == 0:  # scale rts to integer to avoid floating-point inaccuracies...
                    return rts
                else:
                    print('Value must be a multiple of (0.05).')
            else:
                print('Value must be between (0) and (1).')

        except ValueError:
            print('You must enter a numeric value.')


## Dramatic introduction:
print('The fictional world\'s most fearsome card-users...')
time.sleep(1)
print('\nPit against one another in a game of simulated WAR.')
time.sleep(2)

## Setting up the game:
player1, player2 = choose_ur_char()

com = Deck()
com.shuffle()

## Split the deck between each Player (half the deck (52) == 26):
for i in range(26):
    player1.add_cards(com.deal_one())
    player2.add_cards(com.deal_one())

cc = card_count()

rts = round_sleep()

## Main game logic:
game_on = True
turn_ct = 0

while game_on:

    turn_ct += 1
    print(f'Round {turn_ct}')
    time.sleep(rts)

    p1_cards = []
    p1_cards.append(player1.remove_one())

    p2_cards = []
    p2_cards.append(player2.remove_one())

    at_war = True

    while at_war:

        if p1_cards[-1].value > p2_cards[-1].value:

            player1.add_cards(p1_cards)
            player1.add_cards(p2_cards)
            at_war = False
        
        elif p1_cards[-1].value < p2_cards[-1].value:

            player2.add_cards(p2_cards)
            player2.add_cards(p1_cards)
            at_war = False
        
        else:

            print('WAR!')
            time.sleep(1)

            if len(player1.all_cards) < cc:

                print(f'{player1.name} (P1) does not have enough cards ({cc} req\'d) to declare War...\n{player2.name.upper()} (P2) WINS!')
                game_on = False
                break

            elif len(player2.all_cards) < cc:

                print(f'{player2.name} (P2) does not have enough cards ({cc} req\'d) to declare War...\n{player1.name.upper()} (P2) WINS!')
                game_on = False
                break

            else:

                for i in range(cc):

                    p1_cards.append(player1.remove_one())
                    p2_cards.append(player2.remove_one())

    if len(player1.all_cards) == 0:

        print(f'{player1.name} (P1) is out of cards...\n{player2.name.upper()} (P2) WINS!')
        game_on == False
        break

    if len(player2.all_cards) == 0:

        print(f'{player2.name} (P2) is out of cards...\n{player1.name.upper()} (P1) WINS!')
        game_on == False
        break