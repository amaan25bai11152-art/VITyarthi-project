import random

# Build a real 52-card deck
RANKS = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
SUITS = [
    ('clubs', 'black'),
    ('spades', 'black'),
    ('diamonds', 'red'),
    ('hearts', 'red')
]

BASE_VALUES = {
    'ace': 11,
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'jack': 10, 'queen': 10, 'king': 10
}

def make_deck():
    deck = []
    for rank in RANKS:
        for suit, color in SUITS:
            deck.append({'rank': rank, 'suit': suit, 'color': color, 'value': BASE_VALUES[rank]})
    random.shuffle(deck)
    return deck

def hand_value(hand):
    total = sum(card['value'] for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'ace')
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def format_card(card):
    return f"{card['rank'].capitalize()} of {card['suit']} ({card['color']})"

def show_hand(label, hand, reveal_all=True):
    if reveal_all:
        cards_str = ", ".join(format_card(c) for c in hand)
        print(f"{label}: {cards_str} → score {hand_value(hand)}")
    else:
        visible = format_card(hand[0])
        print(f"{label}: {visible}, [hidden]")

def initial_deal(deck):
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    return player, dealer

def dealer_play(deck, dealer):
    while hand_value(dealer) < 17:
        dealer.append(deck.pop())
        print(f"Dealer hits: {format_card(dealer[-1])} → dealer score {hand_value(dealer)}")
    print("Dealer stands.")
    return dealer

def result(player, dealer):
    p = hand_value(player)
    d = hand_value(dealer)
    print(f"\nFinal scores → You: {p} | Dealer: {d}")
    if p > 21:
        return "lose"
    if d > 21:
        return "win"
    if p > d:
        return "win"
    if p < d:
        return "lose"
    return "tie"

def play_round():
    deck = make_deck()
    player, dealer = initial_deal(deck)

    print("\n=== New Round ===")
    show_hand("Your hand", player, reveal_all=True)
    show_hand("Dealer's hand", dealer, reveal_all=False)
    print(f"Dealer visible score: {hand_value([dealer[0]])}\n")

    while True:
        if hand_value(player) == 21 and len(player) == 2:
            print("Blackjack!")
            break

        choice = input("Hit or Stand? ").strip().lower()
        if choice == "hit":
            player.append(deck.pop())
            print(f"You drew: {format_card(player[-1])}")
            print(f"Your hand → score {hand_value(player)}")
            if hand_value(player) > 21:
                print("You bust!")
                break
        elif choice == "stand":
            print("You stand.")
            break
        else:
            print("Please type 'hit' or 'stand'.")

    if hand_value(player) <= 21:
        print("\nDealer reveals:")
        show_hand("Dealer's hand", dealer, reveal_all=True)
        dealer_play(deck, dealer)

    outcome = result(player, dealer)
    if outcome == "win":
        print("You win this round!")
    elif outcome == "lose":
        print("Dealer wins this round.")
    else:
        print("It's a tie.")
    return outcome

def play_set():
    wins = 0
    for i in range(1, 6):  # play 5 rounds
        print(f"\n--- Round {i} of 5 ---")
        outcome = play_round()
        if outcome == "win":
            wins += 1
    print(f"\nSet complete! You won {wins} out of 5 rounds.")
    return wins

def main():
    while True:
        wins = play_set()
        if wins >= 3:
            again = input("You qualified! Play another set? (y/n): ").strip().lower()
            if again != 'y':
                print("Thanks for playing!")
                break
        else:
            print("You did not qualify. Game over.")
            break

if __name__ == "__main__":
    main()