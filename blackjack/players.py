from typing import List
from .card_components import Card


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards: List[Card] = []
        
    def reset_hand(self):
        self.all_cards = []
    
    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


class Dealer(Player):

    pass