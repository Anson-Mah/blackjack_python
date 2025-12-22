import os
import random

# -----------------------------
# Utility
# -----------------------------

def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')


# -----------------------------
# Card / Deck Logic
# -----------------------------

card_values = {
	'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
	'7': 7, '8': 8, '9': 9, '10': 10,
	'J': 10, 'Q': 10, 'K': 10,
	'A': 11, 'B': 1
}

deck = []

def make_deck(num_decks):
	global deck
	deck.clear()
	ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
	for _ in range(num_decks):
		for r in ranks:
			for _ in range(4):
				deck.append(r)
	random.shuffle(deck)


def return_hand_total(hand):
	total = 0
	soft = False

	for c in hand:
		total += card_values[c]

	if total > 21 and 'A' in hand:
		temp = hand[:]
		while 'A' in temp and total > 21:
			idx = temp.index('A')
			temp[idx] = 'B'
			total = sum(card_values[c] for c in temp)
		soft = total <= 21

	return total, soft


# -----------------------------
# Hand Model
# -----------------------------

def create_hand(cards, bet):
	return {
		"cards": cards,
		"bet": bet,
		"active": True,
		"busted": False
	}


# -----------------------------
# Gameplay
# -----------------------------

money = 1000
amount_of_decks = 2
hit_on_soft17 = False


def play_hand(hand, dealer_cards, player_hands, hand_index):
	global money, deck

	while hand["active"]:
		clear_terminal()
		total, _ = return_hand_total(hand["cards"])

		print("-------------------------")
		print(f"Playing Hand {hand_index + 1} of {len(player_hands)}")
		print(f"Bet: ${hand['bet']}")
		print(f"\nDealer Cards: {dealer_cards[0]}, ?\n")

		for idx, h in enumerate(player_hands):
			t = return_hand_total(h["cards"])[0]
			marker = " <-- CURRENT" if idx == hand_index else ""
			print(f"Hand {idx + 1}: {', '.join(h['cards'])} ({t}){marker}")

		print("\nActions:")
		print("[1]. Hit")
		print("[2]. Stand")
		print("[3]. Double Down")
		print("[4]. Split")

		try:
			choice = int(input("Select an Option: "))
		except ValueError:
			continue

		# Hit
		if choice == 1:
			hand["cards"].append(deck.pop(0))
			if return_hand_total(hand["cards"])[0] > 21:
				hand["busted"] = True
				hand["active"] = False
				money -= hand["bet"]

		# Stand
		elif choice == 2:
			hand["active"] = False

		# Double Down
		elif choice == 3:
			if money >= hand["bet"]:
				money -= hand["bet"]
				hand["bet"] *= 2
				hand["cards"].append(deck.pop(0))
				if return_hand_total(hand["cards"])[0] > 21:
					hand["busted"] = True
				hand["active"] = False

		# Split (unlimited, including aces)
		elif choice == 4:
			cards = hand["cards"]
			if (
				len(cards) == 2 and
				card_values[cards[0]] == card_values[cards[1]] and
				money >= hand["bet"]
			):
				money -= hand["bet"]

				c1, c2 = cards
				hand["cards"] = [c1, deck.pop(0)]

				new_hand = create_hand(
					[c2, deck.pop(0)],
					hand["bet"]
				)
				player_hands.insert(hand_index + 1, new_hand)


def dealer_turn(dealer_cards):
	while True:
		total, soft = return_hand_total(dealer_cards)

		if total < 17:
			dealer_cards.append(deck.pop(0))
		elif total == 17 and soft and hit_on_soft17:
			dealer_cards.append(deck.pop(0))
		else:
			break


def play():
	global money

	make_deck(amount_of_decks)
	# for _ in range(6):
		# deck.insert(0, '2')
	bet = 100

	while money > 0:
		if len(deck) < 30:
			make_deck(amount_of_decks)

		dealer_cards = []
		player_hands = [create_hand([], bet)]

		# Initial deal
		for _ in range(2):
			for hand in player_hands:
				hand["cards"].append(deck.pop(0))
			dealer_cards.append(deck.pop(0))

		# Player turn
		i = 0
		while i < len(player_hands):
			play_hand(player_hands[i], dealer_cards, player_hands, i)
			i += 1

		# Dealer turn
		dealer_turn(dealer_cards)
		dealer_total = return_hand_total(dealer_cards)[0]

		clear_terminal()
		print("-------------------------")
		print(f"Dealer Cards: {', '.join(dealer_cards)} ({dealer_total})\n")

		# Resolve hands
		for idx, hand in enumerate(player_hands, start=1):
			total = return_hand_total(hand["cards"])[0]
			print(f"Hand {idx}: {', '.join(hand['cards'])} ({total})")

			if hand["busted"]:
				continue
			elif dealer_total > 21 or total > dealer_total:
				money += hand["bet"] * 2
			elif total == dealer_total:
				money += hand["bet"]

		print(f"\nBalance: ${money}")
		input("\nPress Enter to continue...")


# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
	play()