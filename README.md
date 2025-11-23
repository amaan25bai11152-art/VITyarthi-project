# VITyarthi-project
Simple Python Blackjack ♠️♦️

A lightweight, text-based command-line implementation of the classic casino game Blackjack. This project simulates the game logic, including betting, deck shuffling, and dealer AI.

🎮 Features

Betting System: Start with $1,000 and try to increase your bankroll.
Round Tracking: The game tracks and displays the specific round number for every win/loss event (e.g., "Dealer won Round 3").
Dealer Logic: The dealer automatically plays according to standard rules (hits until reaching 17).
Ace Handling: Automatically calculates Aces as 1 or 11 to prevent busting.
Infinite Play: The game continues until you run out of money or choose to quit.

🚀 How to Run

Prerequisites

You need Python 3.6+ installed on your computer (this project uses f-strings).
Installation
Clone this repository or download the source code.
git clone [https://github.com/yourusername/blackjack-python.git](https://github.com/yourusername/blackjack-python.git)

Navigate to the directory.

cd blackjack-python


Usage
Run the script using Python:
python blackjack.py


📜 How to Play

Place your bet: You enter an amount (up to your total current money).
Check your hand: You get two cards, and the dealer shows one.

Choose action:
Type h to Hit (take another card).
Type s to Stand (keep your current hand).

Win Condition:
Get closer to 21 than the dealer without going over.
If you bust (go over 21), you lose immediately.
If the dealer busts, you win.
📸 Example Output

--- Round 1 (Money: $1000) ---
Bet amount: 100
Your Hand: [('K', 'Hearts'), ('4', 'Clubs')] (Score: 14)
Dealer shows: ('9', 'Spades')
Hit or Stand? (h/s): h
Your Hand: [('K', 'Hearts'), ('4', 'Clubs'), ('5', 'Diamonds')] (Score: 19)
Dealer shows: ('9', 'Spades')
Hit or Stand? (h/s): s

Final Scores -> You: 19 | Dealer: 18
You won Round 1


🛠️ Built With

Python - Core logic

Random Module - Card shuffling

