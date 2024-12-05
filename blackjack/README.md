# Python Blackjack Game

A simple command-line blackjack game implemented in Python.

## Features
- Single-player gameplay against the dealer
- Visual card representation in the terminal
- Chip-based betting system (white $1, red $5, green $25, black $100, purple $500, orange $1000)
- Account balance tracking with transaction history
- Interactive gameplay with options to hit, stand, or double down

## Installation

1. Clone the python-portfolio repository:
```bash
git clone [your-repository-url]
cd python-portfolio/blackjack
```

2. Create and activate a new conda environment (optional but recommended):
```bash
conda create -n blackjack python=3.8
conda activate blackjack
```
- (Refer to my [aws-iam-credential-report](https://github.com/dynamic-stall/aws-iam-credential-report/) repo for Miniconda installation assistance, if Python is not present on your system.)

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
python-portfolio/
└── blackjack/
    ├── __init__.py
    ├── constants.py        # Game constants (cards, chips)
    ├── card_components.py  # Card, Deck, and Hand classes
    ├── players.py          # Player and Dealer classes
    ├── account.py          # Account management for betting
    ├── game.py             # Main game logic
    ├── main.py             # Entry point
    ├── README.md           # (This file)
    └── requirements.txt    # Required packages
```

## How to Play

1. Run the game as a module with the ```-m``` flag from the directory containing the _blackjack_ folder (i.e., from _python-portfolio_):
```bash
python3 -m blackjack.main
```

2. Enter your name when prompted

3. Place bets using chip colors:
   - Format: "[number] [color] [number] [color] ..."
   - Example: "2 black 1 green" for $225 ($100 x 2 + $25)

4. Game Actions:
   - `hit`: Draw another card
   - `stand`: Keep current hand
   - `double`: Double your bet and receive one more card (only available on initial hand)

5. Win Conditions:
   - Get closer to 21 than the dealer without going over
   - Dealer busts (goes over 21)
   - Initial two cards totaling 21 (Blackjack)

## Note
This game uses pandas for transaction tracking. Make sure you have it installed via the ```requirements.txt``` file.

## Future Improvements
- Multiple player support
- Split pairs option
- Insurance bets
- Save game progress
- Statistics tracking