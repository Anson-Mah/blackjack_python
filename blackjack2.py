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
		print('[4]. Explain Settings')
		print('[5]. How to Play Blackjack')

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
	global amount_of_decks, surrender, hit_on_17
	make_deck(amount_of_decks)

# Creates decks for the game
def make_deck(amount_of_decks):
	global deck
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	for i in range(amount_of_decks):
		for j in range(len(ranks)):
			for k in range(4):
				deck.append(ranks[j])
	random.shuffle(deck)

# Creates empty deck. Will be used later for game purposes.
deck = []		

# Settings
amount_of_decks = 2
surrender = False
hit_on_17 = False

if __name__ == "__main__":
	main()