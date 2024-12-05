from .constants import chips
from .card_components import Deck, Hand
from .players import Player, Dealer
from .account import Account


class BlackjackGame:

    def __init__(self, player_name, initial_balance=10000):
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer("Dealer")
        self.player_account = Account(player_name, initial_balance)
        self.current_bet = 0
        self.player_hand = None
        self.dealer_hand = None

    def place_bet(self):
        while True:
            print("\nAvailable chips:", ', '.join(f"{color}(${value})" for color, value in chips.items()))
            print(f"Current balance: {self.player_account.get_balance()}")
            
            bet_input = input("\nEnter your bet using chip colors (e.g., '2 black 1 green' for $225): ")
            total_bet = 0
            
            try:
                bet_parts = bet_input.lower().split()
                for i in range(0, len(bet_parts), 2):
                    count = int(bet_parts[i])
                    color = bet_parts[i + 1]
                    if color in chips:
                        total_bet += count * chips[color]
                    else:
                        print("Invalid chip color!")
                        break
                
                if total_bet <= float(self.player_account.get_balance().replace('$', '')):
                    self.current_bet = total_bet
                    self.player_account.withdraw(total_bet)
                    print(f"\nBet placed: ${total_bet}")
                    break
                else:
                    print("Insufficient funds!")
            except (ValueError, IndexError):
                print("Invalid bet format! Use: <number> <color> [<number> <color> ...]")
    
    def deal_initial_cards(self):
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        # Deal cards alternately
        self.player_hand.add_card(self.deck.deal_one())
        self.dealer_hand.add_card(self.deck.deal_one())
        self.player_hand.add_card(self.deck.deal_one())
        self.dealer_hand.add_card(self.deck.deal_one())
    
    def player_turn(self):
        while True:
            print("\nYour hand:")
            self.player_hand.print_hand()
            print(f"Your total: {self.player_hand.value}")
            
            print("\nDealer's hand:")
            self.dealer_hand.print_hand(hide_first=True)
            
            if self.player_hand.value == 21:
                print("BLACKJACK!")
                return
            
            if self.player_hand.value > 21:
                print("Bust!")
                return
            
            action = input("\nWhat would you like to do? (hit/stand/double): ").lower()
            
            if action == 'hit':
                self.player_hand.add_card(self.deck.deal_one())
            elif action == 'double':
                if len(self.player_hand.cards) == 2:
                    if self.current_bet <= float(self.player_account.get_balance().replace('$', '')):
                        self.player_account.withdraw(self.current_bet)
                        self.current_bet *= 2
                        self.player_hand.add_card(self.deck.deal_one())
                        print("\nYour final hand:")
                        self.player_hand.print_hand()
                        print(f"Your total: {self.player_hand.value}")
                        return
                    else:
                        print("Insufficient funds to double down!")
                else:
                    print("Can only double down on initial hand!")
            elif action == 'stand':
                return
    
    def dealer_turn(self):
        print("\nDealer's full hand:")
        self.dealer_hand.print_hand()
        
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_one())
            print("\nDealer hits:")
            self.dealer_hand.print_hand()
            print(f"Dealer's total: {self.dealer_hand.value}")
    
    def determine_winner(self):
        player_value = self.player_hand.value
        dealer_value = self.dealer_hand.value
        
        print(f"\nYour total: {player_value}")
        print(f"Dealer's total: {dealer_value}")
        
        if player_value > 21:
            print("You bust! Dealer wins!")
            return False
        elif dealer_value > 21:
            print("Dealer busts! You win!")
            self.player_account.deposit(self.current_bet * 2)
            return True
        elif player_value > dealer_value:
            print("You win!")
            self.player_account.deposit(self.current_bet * 2)
            return True
        elif dealer_value > player_value:
            print("Dealer wins!")
            return False
        else:
            print("Push!")
            self.player_account.deposit(self.current_bet)
            return None
    
    def play(self):
        while True:
            # Start new round
            print("\n" + "=" * 50)
            print(f"Grab a seat, {self.player.name}!")
            
            self.place_bet()
            self.deal_initial_cards()
            
            self.player_turn()
            if self.player_hand.value <= 21:
                self.dealer_turn()
            self.determine_winner()
            
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print(f"\nFinal balance: {self.player_account.get_balance()}")
                print("Thanks for playing!")
                break
            
            # Reset deck if running low
            if len(self.deck.all_cards) < 15:
                self.deck = Deck()