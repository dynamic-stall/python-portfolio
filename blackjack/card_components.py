from typing import List
from random import shuffle
from .constants import suits, ranks, values, rank_viz, suit_viz


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.rank_viz = rank_viz[ranks.index(rank)]
        self.suit_viz = suit_viz[suits.index(suit)]
        
    def get_blackjack_value(self, current_total=0):
        if self.rank == 'Ace':
            return 11 if current_total + 11 <= 21 else 1
        return min(10, self.value)


class Deck:

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
                
    def shuffle(self):
        shuffle(self.all_cards)
        
    def deal_one(self):
        if not self.all_cards:
            raise ValueError('No cards left in the deck!')
        return self.all_cards.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.calculate_value()
    
    def calculate_value(self):
        self.value = 0
        self.aces = 0
        
        for card in self.cards:
            if card.rank == 'Ace':
                self.aces += 1
            self.value += card.get_blackjack_value()
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def print_hand(self, hide_first=False):
        for i, card in enumerate(self.cards):
            if i == 0 and hide_first:
                print("+-------+")
                print("|  ***  |")
                print("|  ***  |")
                print("|  ***  |")
                print("+-------+")
            else:
                print("+-------+")
                print(f"| {card.rank_viz.ljust(2)}    |")
                print(f"|   {card.suit_viz}   |")
                print(f"|    {card.rank_viz.rjust(2)} |")
                print("+-------+")