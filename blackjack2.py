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
	global deck, money, amount_of_decks, insurance, surrender, hit_on_soft17
	make_deck(amount_of_decks)

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
			print(f"Your bet has been set to ${bet}.")
			break


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
	global amount_of_decks, insurance, surrender, hit_on_soft17
	print("Current Settings")
	print("-----------------")
	print(f"Amount of Decks: {amount_of_decks}")
	print(f"Insurance: {'Enabled' if insurance == True else 'Disabled'}")
	print(f"Surrender: {'Enabled' if surrender == True else 'Disabled'}")
	print(f"Hit on Soft 17: {'Enabled' if hit_on_soft17 == True else 'Disabled'}")


def change_settings():
	global amount_of_decks, insurance, surrender, hit_on_soft17

	# Settings Menu
	print("Which setting would you like to change?")
	print("-----------------------------------------")
	print("[0]. Exit Settings")
	print("[1]. Amount of Decks")
	print("[2]. Insurance")
	print("[3]. Surrender")
	print("[4]. Hit on Soft 17")
	print("[5]. Restore Default Settings")

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
					print(f"Amount of Decks set to {amount_of_decks}\n")
					break
		case 2:
			# Insurance
			if insurance == True:
				insurance = False
			else:
				insurance = True
			clear_terminal()
			print(f"Insurance set to {insurance}\n")
		case 3:
			# Surrender
			if surrender == True:
				surrender = False
			else:
				surrender = True
			clear_terminal()
			print(f"Surrender set to {surrender}\n")
		case 4:
			# Hit on 17
			if hit_on_soft17 == True:
				hit_on_soft17 = False
			else:
				hit_on_soft17 = True
			clear_terminal()
			print(f"Hit on 17 set to {hit_on_soft17}")
		case 5:
			# Restore Default Settings
			amount_of_decks = 2
			insurance = True
			surrender = True
			hit_on_soft17 = False
			clear_terminal()
			print("Default Settings have been restored.\n")

	change_settings()


def explain_settings():
	print("AMOUNT OF DECKS:")
	print("Determines the amount of decks that will be shuffled with each new shoe.")

	print("")

	print("INSURANCE:")
	print("Before a player begins playing their hand, they may buy insurance.")
	print("Insurance is equal to the bet initially made, and is given back to the player if the dealer does in fact have a blackjack.")
	print("If the dealer is dealt a Blackjack, they receive back their original bet.")

	print("")

	print("SURRENDER:")
	print("Before a player begins playing their hand, they may choose to Surrender their hand.")
	print("Surrendering makes you automatically give your hand back to the dealer.")
	print("You receive back half of your original bet, while the other half goes to the dealer.")

	print("")

	print("HIT ON SOFT 17:")
	print("By default, the dealer will automatically stand on all hands worth 17.")
	print("Enabling this setting will change that behavior, making the dealer hit on a Soft 17.")
	print("A Soft Hand is a hand that contains an 11-valued Ace. It is called a Soft hand because you cannot bust if you take another card.")
	print("Note that even with this setting enabled, the dealer will still stand on a Hard 17 (A hand worth 17 but does not have an 11-valued Ace.)")


def how_to_play():
	print("How to Play: Blackjack")

	print()

	print("The objective of the game is to bet against the dealer for hands as close to 21 as possible without going over.")

	print()

	print("Cards from 2-10 are worth their face value. ")
	print("Face cards are worth 10. ")
	print("Aces are worth 11 or 1, depending on which is more advantageous to the hand. ")
	print("Players make their bets on the round, then the dealer passes out one card face up to everyone including themselves. ")
	print("Next, the dealer passes out one more card face up to all of the players and one card face down for their own hand. ")
	print("If you are dealt 21, this is called a BLACKJACK, if the dealer does not also have a BLACKJACK, then you immediately win an amount equal to 1.5 times your initial bet and the round ends.")

	print()

	print("You (The Player) will always first play your hand before the dealer reveals their face down card. ")
	print("Before a player begins playing their hand; they may opt to do one, both, or none of the following: BUY INSURANCE, or SURRENDER. ")
	print("A player may BUY INSURANCE in case the dealer has a blackjack. ")
	print("Insurance is equal to the bet initially made, and is given back to the player if the dealer does in fact have a blackjack. ")
	print("Additionally, a player may SURRENDER their hand if they are confident that they will lose. ")
	print("Surrendering gives the player back half of their bet, while the other half is given to the dealer. ")
	print("After this, the dealer checks their hand to if they have a BLACKJACK. ")
	print("If they do, they reveal their BLACKJACK immediately and the round ends.")

	print()

	print("You can choose to HIT, meaning to request an additional card from the deck. ")
	print("If your hand becomes over 21 after hitting, this is called a BUST and you automatically lose your bet. ")
	print("You may HIT as many times as you like, as long as you do not BUST. ")

	print()

	print("You can also choose to STAND, ending your turn and keeping the cards dealt to you. ")
	print("You can stand before or after hitting.")

	print()

	print("You can decide to SPLIT your cards only if the 2 cards originally dealt to you are a pair. ")
	print("Splitting turns the pair into two individual hands, each with their own bet equal to the player’s first bet. ")
	print("The dealer then deals you two additional cards to complete each hand and the game continues, with you playing both hands normally. ")

	print()

	print("You can decide to DOUBLE DOWN and double your initial bet. ")
	print("If you decide to DOUBLE DOWN, the dealer will give you one more card after which you must stand.")

	print()

	print("Once you have finished playing your hand, the dealer's turn begins.")
	print("The dealer begins their turn by revealing their facedown card.")
	print("Unlike the player, the dealer has specific rules regarding their play which must be followed at all times.")
	print("If the dealer has anything under 17, then the must HIT.")
	print("If the dealer has 17 or over, then they must STAND.")
	print("Once the dealer finishes playing their hand, you compare your hand against the dealer's")

	print()

	print("If the dealer's hand is closer to 21 than yours, you lose your entire bet. ")
	print("If your hand is closer to 21 than the dealer's, you win an amount equal to your bet. ")
	print("If the dealer busts, you win an amount equal to your bet. ")
	print("If you and your dealer have the same value, then you PUSH (Tie), and no exchange of bets is made.")

	print()

	print("After each round, all the cards in play are discarded but not shuffled back into the deck. ")
	print("Only once all the cards in the deck have been used is it shuffled.")

	print()

	print('The great majority of script has been directly ripped from the Youtube video "How to play Blackjack" created by Triple S. Games')
	print("Minor changes have been made, adjusting the script to fit readers rather than listeners.")


def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')


# Creates empty deck. Will be used later for game purposes.
deck = []		

# Game Settings
amount_of_decks = 2
surrender = True
hit_on_soft17 = False
insurance = True

# Money
money = 100

if __name__ == "__main__":
	main()