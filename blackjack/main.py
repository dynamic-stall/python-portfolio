from .game import BlackjackGame
import time

def main():
    print('Welcome to Blackjack!')
    time.sleep(1.5)
    print('Let\'s play a round or three... ;)')
    time.sleep(1.5)
    game = BlackjackGame(input('May I have your name? '))
    print('It\'s a pleasure to meet you! "Dōzo yoroshiku," as they say in Japanese...')
    time.sleep(3)
    game.play()

if __name__ == "__main__":
    main()