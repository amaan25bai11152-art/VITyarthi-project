import random
import time
import os

# --- Game Constants ---
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


def clear_screen():
    """Clears the console screen for a cleaner game view."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_deck():
    """Creates a standard 52-card deck."""
    return [(rank, suit) for suit in SUITS for rank in RANKS]


def calculate_score(hand):
    """Calculates the score of a hand, handling Aces automatically."""
    score = 0
    aces = 0

    for rank, suit in hand:
        score += VALUES[rank]
        if rank == 'A':
            aces += 1

    # Adjust for Aces if score is over 21
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def display_hands(player_hand, bot_hand, hide_bot_card=True):
    """Prints the current state of the table."""
    print("\n" + "=" * 40)

    # Display Bot's Hand
    print("🤖  BOT (DEALER) HAND:")
    if hide_bot_card:
        # Show first card, hide the second
        print(f"   [{bot_hand[0][0]}{bot_hand[0][1]}] [??]")
    else:
        cards_str = " ".join([f"[{r}{s}]" for r, s in bot_hand])
        print(f"   {cards_str}  (Score: {calculate_score(bot_hand)})")

    print("-" * 40)

    # Display Player's Hand
    print("👤  YOUR HAND:")
    cards_str = " ".join([f"[{r}{s}]" for r, s in player_hand])
    print(f"   {cards_str}  (Score: {calculate_score(player_hand)})")

    print("=" * 40 + "\n")


def get_bet(current_money):
    """Asks the user for a valid bet amount."""
    while True:
        try:
            print(f"\n💰 Current Balance: ${current_money}")
            bet_input = input("💵 Enter your bet amount: ")
            bet = int(bet_input)

            if bet <= 0:
                print("❌ Bet must be greater than 0.")
            elif bet > current_money:
                print("❌ You don't have enough money!")
            else:
                return bet
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def play_round(round_num, current_money):
    """Runs the logic for a single round. Returns the net profit/loss."""
    clear_screen()
    print(f"\n📢 --- STARTING ROUND {round_num} / 5 ---")

    # 1. Place Bet
    bet = get_bet(current_money)
    print(f"✅ Bet placed: ${bet}")
    time.sleep(1)

    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    bot_hand = [deck.pop(), deck.pop()]

    # --- Player Turn ---
    while True:
        clear_screen()
        print(f"📌 ROUND {round_num} OF 5 | BET: ${bet}")
        display_hands(player_hand, bot_hand, hide_bot_card=True)

        player_score = calculate_score(player_hand)

        if player_score == 21:
            print("🎉 BLACKJACK! You got 21!")
            time.sleep(1)
            break
        if player_score > 21:
            print("💥 BUST! You went over 21.")
            time.sleep(1)
            break

        choice = input("👉 Action: [H]it or [S]tand? ").lower().strip()

        if choice.startswith('h'):
            print("🃏 Dealing card...")
            time.sleep(0.5)
            player_hand.append(deck.pop())
        elif choice.startswith('s'):
            print("🛑 You chose to stand.")
            time.sleep(0.5)
            break
        else:
            print("❌ Invalid input. Please type 'H' or 'S'.")
            time.sleep(1)

    player_score = calculate_score(player_hand)

    # --- Bot Turn ---
    if player_score <= 21:
        print("\n🤖 Bot is thinking...")
        time.sleep(1)

        while True:
            bot_score = calculate_score(bot_hand)
            # Show update
            clear_screen()
            print(f"📌 ROUND {round_num} OF 5 | BET: ${bet}")
            display_hands(player_hand, bot_hand, hide_bot_card=False)

            if bot_score < 17:
                print("🤖 Bot HITS.")
                time.sleep(1)
                bot_hand.append(deck.pop())
            else:
                print("🤖 Bot STANDS.")
                time.sleep(1)
                break

    # --- Determine Winner & Result Screen ---
    # We clear screen here so the result is the ONLY thing focusing the user
    clear_screen()
    bot_score = calculate_score(bot_hand)

    print("\n" + "📢" * 30)
    print(f"         ROUND {round_num} RESULT")
    print("📢" * 30 + "\n")

    # Show final hands explicitly with cards
    print("🤖  BOT (DEALER) FINAL HAND:")
    cards_str = " ".join([f"[{r}{s}]" for r, s in bot_hand])
    print(f"   {cards_str}  (Score: {bot_score})")

    print("-" * 40)

    print("👤  YOUR FINAL HAND:")
    cards_str = " ".join([f"[{r}{s}]" for r, s in player_hand])
    print(f"   {cards_str}  (Score: {player_score})")

    print("=" * 40 + "\n")

    winner_code = ""  # "player", "bot", "draw"
    profit = 0

    # --- Logic to Determine Winner ---
    if player_score > 21:
        print(f"❌ YOU BUSTED! (Over 21)")
        print(f"💸 YOU LOST ${bet}")
        print("\n" + "🟥" * 20 + "  BOT WON  " + "🟥" * 20)
        winner_code = "bot"
        profit = -bet
    elif bot_score > 21:
        print(f"🎉 BOT BUSTED! (Bot went over 21)")
        print(f"💰 YOU WON ${bet}!")
        print("\n" + "🟩" * 20 + "  YOU WON  " + "🟩" * 20)
        winner_code = "player"
        profit = bet
    elif player_score > bot_score:
        print(f"🎉 HIGHER SCORE! ({player_score} vs {bot_score})")
        print(f"💰 YOU WON ${bet}!")
        print("\n" + "🟩" * 20 + "  YOU WON  " + "🟩" * 20)
        winner_code = "player"
        profit = bet
    elif bot_score > player_score:
        print(f"❌ BOT HAS HIGHER SCORE ({bot_score} vs {player_score})")
        print(f"💸 YOU LOST ${bet}")
        print("\n" + "🟥" * 20 + "  BOT WON  " + "🟥" * 20)
        winner_code = "bot"
        profit = -bet
    else:
        print(f"🤝 PUSH! (It's a Tie)")
        print(f"↩️  Money Returned")
        print("\n" + "🟨" * 20 + "   DRAW    " + "🟨" * 20)
        winner_code = "draw"
        profit = 0

    print("\n")
    input("👉 Press Enter to start the next round...")
    return winner_code, profit


def main():
    while True:
        clear_screen()
        print("\n" + "#" * 50)
        print("      🎲  PYTHON BLACKJACK: VEGAS STYLE  🎲")
        print("          5-Round Match vs Bot Dealer")
        print("#" * 50)
        input("\nPress Enter to Start...")

        money = 1000  # Starting money
        player_wins = 0
        bot_wins = 0
        draws = 0

        # 5 Round Loop
        for i in range(1, 6):
            if money <= 0:
                print("\n💀 YOU ARE BROKE! GAME OVER.")
                break

            winner, profit = play_round(i, money)
            money += profit

            if winner == "player":
                player_wins += 1
            elif winner == "bot":
                bot_wins += 1
            else:
                draws += 1

        # --- Match Over ---
        clear_screen()
        print("\n" + "🏆" * 20)
        print("           MATCH FINISHED           ")
        print("🏆" * 20 + "\n")

        print(f"💵 Final Balance: ${money}")
        print(f"👤 Player Wins:   {player_wins}")
        print(f"🤖 Bot Wins:      {bot_wins}")
        print(f"🤝 Draws:         {draws}")
        print("-" * 30)

        if money > 1000:
            print(f"🤑 PROFIT! You made ${money - 1000} profit!")
        elif money < 1000:
            print(f"📉 LOSS. You lost ${1000 - money}.")
        else:
            print("😐 BREAK EVEN. No money lost or gained.")

        print("\n" + "=" * 50)
        replay = input("Play another match? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Bye!")
            break


if __name__ == "__main__":
    main()