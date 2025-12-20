import random
import os

def main():
	while True:
		# Initial Menu
		print("-------------------------")
		print("[0]. Quit Program")
		print('[1]. Play Blackjack')
		print("[2]. View Settings")
		print("[3]. Change Settings")
		# print('[4]. Explain Settings')
		# print('[5]. How to Play Blackjack')

		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		try:
			selection = int(input("Select an Option: "))
		except ValueError:
				# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
			selection = 9

		clear_terminal()

		# Runs different functions based off of what you inputted
		match selection:
			case 0:
				print("Program Terminated")
				exit()
			case 1:
				play()
			case 2:
				view_settings()
			case 3:
				change_settings()
			case 4:
				explain_settings()
			case 5:
				how_to_play()


def play():
	global deck, money, amount_of_decks, hit_on_soft17
	make_deck(amount_of_decks)

	# Creates More In-Game Variables
	player_cards = []
	dealer_cards = []

	# Input Validation for the Bet
	while True:
		try:
			user_bet = float(input("Your Bet: $"))
		except ValueError:
			print("Please input a valid bet.")
			continue
		if user_bet > money:
			print(f"You cannot bet more than you have. You currently have ${money}.")
		elif user_bet < 0:
			print("You cannot have a negative bet. Please input a value greater than 0.")
		elif user_bet == 0:
			print("You cannot bet $0. Please input a value greater than 0.")
		else:
			bet = user_bet
			clear_terminal()
			print(f"Your bet has been set to ${bet}.\n")
			break

	# Deal Out Cards
	for i in range(4):
		random_card = random.choice(deck)
		deck.remove(random_card)
		if i % 2 == 0:
			player_cards.append(random_card)
		else:
			dealer_cards.append(random_card)
		# print(i, i%2, random_card)

	# Display Cards in Play
	print(f"Dealer Cards: {dealer_cards[0]}, ?")	
	print(f"Player Cards: {", ".join(player_cards)}")  # The ", ".join(cards) syntax is used to remove brackets and quotation marks when printing the list


# Creates decks for the game
def make_deck(amount_of_decks):
	global deck
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	for i in range(amount_of_decks):
		for j in range(len(ranks)):
			for k in range(4):
				deck.append(ranks[j])
	random.shuffle(deck)


def view_settings():
	global amount_of_decks, hit_on_soft17
	print("Current Settings")
	print("-----------------")
	print(f"Amount of Decks: {amount_of_decks}")
	print(f"Hit on Soft 17: {'Enabled' if hit_on_soft17 == True else 'Disabled'}")


def change_settings():
	global amount_of_decks, hit_on_soft17

	# Settings Menu
	print("Which settings would you like to change?")
	print("-----------------------------------------")
	print("[0]. Exit Settings")
	print("[1]. Amount of Decks")
	print("[2]. Hit on Soft 17")
	print("[3]. Restore Default Settings")

	# Input Correction
	# If the user's input would break the program, it changes the input such that it will not break the program.
	try:
		selection = int(input("Select an Option: "))
	except ValueError:
		# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
		selection = 9

	match selection:
		case 0:
			clear_terminal()
			main()
		case 1:
			# Amount of Decks
			while True:
				try:
					user_amount_of_decks = int(input("\nInput your desired amount of decks: "))
				except ValueError:
					print("Please input a positive integer.")
					continue
				if user_amount_of_decks <= 0:
					print("You have inputted a non-positive integer. Please input a positive integer.")
				else:
					amount_of_decks = user_amount_of_decks
					clear_terminal()
					print(f"Amount of Decks set to {amount_of_decks}.\n")
					break
		case 2:
			# Hit on 17
			if hit_on_soft17 == True:
				hit_on_soft17 = False
			else:
				hit_on_soft17 = True
			clear_terminal()
			print(f"Hit on Soft 17 has been {'Enabled' if hit_on_soft17 == True else 'Disabled'}.\n")
		case 3:
			# Restore Default Settings
			amount_of_decks = 2
			hit_on_soft17 = False
			clear_terminal()
			print("Default Settings have been restored.\n")

	change_settings()


def explain_settings():
	print("AMOUNT OF DECKS:")
	print("Determines the amount of decks that will be shuffled with each new shoe.")

	print("")

	print("HIT ON SOFT 17:")
	print("By default, the dealer will automatically stand on all hands worth 17.")
	print("Enabling this setting will change that behavior, making the dealer hit on a Soft 17.")
	print("A Soft Hand is a hand that contains an 11-valued Ace. It is called a Soft hand because you cannot bust if you take another card.")
	print("Note that even with this setting enabled, the dealer will still stand on a Hard 17 (A hand worth 17 but does not have an 11-valued Ace.)")


def how_to_play():
	print("How to Play: Blackjack")

	print("")

	print("OBJECTIVE:")
	print("Win money by creating hands that are higher than the dealer's hand but do not exceed 21.")
	
	print("")
	print("")
	
	print("CARD VALUES:")
	print("Cards from 2-10 are worth their face value.")
	print("Face cards are worth 10.")
	print("Aces are worth 11 or 1, depending on which is more advantageous to the hand.")
	
	print("")
	print("")
	
	print("ROUND START:")
	print("You and the dealer are initially dealt two cards each.")
	print("The dealer passes out one card face up to you and themself. ")
	print("Next, the dealer passes out one more card face up to you, but one card face down for their own hand. ")
	
	print("")
	print("")
	
	print("BLACKJACK:")
	print("If your initial two cards make a value of 21, this is called a BLACKJACK.")
	print("If the dealer does not also have a BLACKJACK, then you immediately win an amount equal to 1.5 times your initial bet and the hand immediately ends.")
	
	print("")
	print("")
	
	print("PLAYER DECISIONS:")
	print("You will always take your turn first before the dealer takes their turn.")
	
	print("")
	
	print(" Hit: ")
	print(" Take an additional card from the deck and add it to your hand.")
	print(" If your hand becomes over 21 after hitting, this is called a BUST and you automatically lose your bet.")
	print(" You may hit as many times as you like, as long as you do not bust.")
	
	print("")
	
	print(" Stand: ")
	print(" End your turn and keep all cards dealt to you.")
	
	print("")
	
	print(" Double Down:")
	print(" Double your initial bet and add exactly one more card to your hand.")
	
	print("")
	
	print(" Split:")
	print(" You can decide to split your cards only if the 2 cards originally dealt to you are the same value.")
	print(" Splitting turns the pair into two individual hands, each with their own bet equal to the player's initial bet.")
	print(" The dealer then deals you two additional cards to complete each hand.")
	
	print("")
	
	print(" Surrender:")
	print(" Forfeit half your bet and end the hand immediately.")
	
	print("")
	print("")
	
	print("DEALER'S TURN:")
	print("Once you have finished playing your hand, the dealer's turn begins.")
	print("The dealer begins their turn by revealing their facedown card.")
	print("Unlike the player, the dealer has specific rules regarding their play which must be followed at all times.")
	print("If the dealer has anything under 17, then the must HIT.")
	print("If the dealer has 17 or over, then they must STAND.")
	print("The dealer cannot DOUBLE DOWN nor SPLIT.")
	print("Once the dealer finishes playing their hand, you compare your hand against the dealer's.")
	
	print("")
	
	print("If the dealer's hand is closer to 21 than yours, you lose your entire bet. ")
	print("If your hand is closer to 21 than the dealer's, you win an amount equal to your bet. ")
	print("If the dealer busts, you win an amount equal to your bet. ")
	print("If you and your dealer have the same value, then you PUSH (Tie), and no exchange of bets is made.")


def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')


# Creates empty deck. Will be used later for game purposes.
deck = []		

# Game Settings
amount_of_decks = 2
hit_on_soft17 = False

# Money
money = 1000

if __name__ == "__main__":
	main()