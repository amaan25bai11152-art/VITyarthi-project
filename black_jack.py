import random


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]


def get_score(hand):
    total = sum(values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


money = 1000
round_num = 0



while money > 0:
    round_num += 1
    print(f"\n--- Round {round_num} (Money: ${money}) ---")

    # Create and shuffle deck in one go
    deck = [(r, s) for s in suits for r in ranks]
    random.shuffle(deck)

    bet = int(input("Bet amount: "))
    if bet > money:
        print("Not enough cash.")
        continue

    # Deal cards
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    # Player Turn
    while get_score(player) < 21:
        print(f"Your Hand: {player} (Score: {get_score(player)})")
        print(f"Dealer shows: {dealer[0]}")

        if input("Hit or Stand? (h/s): ").lower() == 'h':
            player.append(deck.pop())
        else:
            break

    # dealer Turn (only when player didn't bust)
    p_score = get_score(player)
    if p_score <= 21:
        while get_score(dealer) < 17:
            dealer.append(deck.pop())

    d_score = get_score(dealer)

    # Determine Winner
    print(f"\nfinal scores -> you: {p_score} | dealer: {d_score}")

    if p_score > 21:
        print(f"bust! dealer won round {round_num}")
        money -= bet
    elif d_score > 21:
        print(f"dealer busts! You won Round {round_num}")
        money += bet
    elif p_score > d_score:
        print(f"You won Round {round_num}")
        money += bet
    elif d_score > p_score:
        print(f"Dealer won Round {round_num}")
        money -= bet
    else:
        print(f"round {round_num} was a draw")

    if input("play again? (y/n): ").lower() != 'y':
        break

print("Game Over!")
