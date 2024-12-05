from .game import BlackjackGame

def main():
    game = BlackjackGame(input("Please enter your name: "))
    game.play()

if __name__ == "__main__":
    main()