import random
import os

def main():
	while True:
		# Initial Menu
		print("-------------------------")
		print("[0]. Quit Program")
		print('[1]. Play "Storts, Chophy, Bascat"')
		print("[2]. View Settings")
		print("[3]. Change Settings")
		print('[4]. Explain Settings')
		print('[5]. How to Play "Storts, Chophy, Bascat"')

		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		while True:
			try:
				selection = int(input("Select an Option: "))
				break
			except ValueError:
				# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
				selection = 9
				break

		clear_terminal()

		# Runs different functions based off of what you inputted
		match selection:
			case 0:
				print("Program Terminated")
				exit()
			case 1:
				play_scb()
			case 2:
				view_settings()
			case 3:
				change_settings()
			case 4:
				explain_settings()
			case 5:
				show_how_to_play()

def play_scb():
	global attempts, word_length, mystery_word_candiates_list, guessable_words_list

	# Resets word lists
	# This accounts for situations where the user changes the word length in between games
	mystery_word_candiates_list = []
	guessable_words_list = []

	get_words()

	# Creates variables used for the game
	word_has_been_guessed = False
	attempts_left = attempts
	attempts_used = 0
	chophy_letters = []
	storts_letters = []
	bascat_letters = []
	unguessed_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	if obscure_words == True:
		mystery_word = random.choice(guessable_words_list)
	else:
		mystery_word = random.choice(mystery_word_candiates_list)

	while word_has_been_guessed == False and attempts_left > 0:
		if attempts_left != 1:
			print(f"You have {attempts_left} attempts remaining.")
		else:
			print(f"You have {attempts_left} attempt remaining.")

		# Displays lists of all letters in a certain category. 
			# Prints all letters that were marked as Chophy, Storts, or Bascat in a previous guess
			# Also prints a list of unguessed letters.
		# The ", ".join(letters) syntax is used to remove brackets and quotation marks when printing the list
		print(f"\nChophy: {", ".join(chophy_letters)}")
		print(f"Storts: {", ".join(storts_letters)}")
		print(f"Bascat: {", ".join(bascat_letters)}")
		print(f"Unguessed: {", ".join(unguessed_letters)}")

		# Input Validation
		# This portion of code loops until the user inputs a valid guess.
		while True:
			try:
				print()
				guess = input(f"Guess a {word_length} letter word: ")
			except ValueError:
				continue
			if not guess.isalpha():
				print("You must type in valid Alphabetical characters.")
			elif len(list(guess.strip())) != word_length:
				print(f"Word must be {word_length} letters long.")
			elif guess not in guessable_words_list:
				print("Not in word list.")
			else:
				guess = guess.strip().lower()
				print()
				break

		attempts_used = attempts_used + 1

		# Ends the game if user has guessed the correct word
		if mystery_word == guess:
			word_has_been_guessed = True
			break
		else:
			attempts_left = attempts_left - 1

			# Removes all guessed letters in this for loop. 
			# The letters then get added back to its appropiate list in the "Letter Checking" for loop
			for i in range(word_length):
				if guess[i] in chophy_letters:
					chophy_letters.remove(guess[i])
				elif guess[i] in storts_letters:
					storts_letters.remove(guess[i])
				elif guess[i] in bascat_letters:
					bascat_letters.remove(guess[i])
				elif guess[i] in unguessed_letters:
					unguessed_letters.remove(guess[i])

			# Letter Checking
			for i in range(word_length):
				if guess[i] in mystery_word and guess[i] == mystery_word[i]:
					print(f"{guess[i]}, {GREEN}Chophy (C){DEFAULT}")
					chophy_letters.append(guess[i])
					continue
				if guess[i] in mystery_word:
					print(f"{guess[i]}, {YELLOW}Storts (S){DEFAULT}")
					storts_letters.append(guess[i])
				else:
					print(f"{guess[i]}, Bascat (B)")
					bascat_letters.append(guess[i])

			# Removes duplicate letters from list
			chophy_letters = list(set(chophy_letters))
			storts_letters = list(set(storts_letters))
			bascat_letters = list(set(bascat_letters))

			# Sorts lists
			chophy_letters.sort()
			storts_letters.sort()
			bascat_letters.sort()

			print()

	# Game End
	if attempts_left == 0:
		print("You have 0 attempts left and lost the game.")
		print(f'The word was "{mystery_word}".')
	else: 
		print(f"Congratulations! You have successfully guessed the word!")
		print(f'The word was "{mystery_word}".')
		if attempts_used != 1:
			print(f"You guessed the word in {attempts_used} attempts.")
		else:
			print(f"You guessed the word in {attempts_used} attempt! You are so sigma for guessing the word in 1 attempt 😎")

def view_settings():
	global word_length, attempts, obscure_words
	print("Current Settings")
	print("-----------------")
	print(f"Word Length: {word_length}")
	print(f"Amount of Attempts: {attempts}")
	if obscure_words == True:
		print("Obscure Words: Enabled")
	else:
		print("Obscure Words: Disabled")

def change_settings():
	global word_length, attempts, obscure_words

	# Settings Menu
	print("Which settings would you like to change?")
	print("-----------------------------------------")
	print("[1]. Word Length")
	print("[2]. # of Attempts")
	print("[3]. Enable/Disable Obscure Words")
	print("[4]. Restore Default Settings")
	print("[5]. Exit Settings")

	# Input Correction
	# If the user's input would break the program, it changes the input such that it will not break the program.
	while True:
		try:
			selection = int(input("\nSelect an Option: "))
			break
		except ValueError:
			# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
			selection = 9
			break

	# Lets user change the settings that they want to change.
	match selection:
		case 1:
			# Word Length
			while True:
				try:
					user_word_length = int(input("\nInput your desired word length: "))
				except ValueError:
					print("Please input a positive integer.")
					continue
				if user_word_length <= 0:
					print("You have inputted a non-positive integer. Please input a positive integer.")
				elif user_word_length > 19:
					print("Unfortunately, there are no words that have your desired word length. Please pick a different number.")
				else:
					word_length = user_word_length
					clear_terminal()
					print(f"Word Length set to {word_length}\n")
					break
		case 2:
			# Amount of Attempts
			while True:
				try:
					user_attempts = int(input("\nInput your desired amount of attempts: "))
				except ValueError:
					print("Please input a positive integer.")
					continue
				if user_attempts <= 0:
					print("You have inputted a non-positive integer. Please input a positive integer.")
				else:
					attempts = user_attempts
					clear_terminal()
					print(f"Amount of attempts set to {attempts}\n")
					break
		case 3:
			if obscure_words == True:
				obscure_words = False
				clear_terminal()
				print("Obscure Words now Disabled")
			else:
				obscure_words = True
				clear_terminal()
				print("Obscure Words now Enabled")
		case 4:
			word_length = 5
			attempts = 6
			obscure_words = False
			clear_terminal()
			print("Default Settings have been restored.\n")
		case 5:
			clear_terminal()
			main()

	change_settings()

def explain_settings():
	print("WORD LENGTH: ")
	print("Determines the amount of letters your words will have.")
	print("The mystery word will have the word length that you set, and your guesses are required to have the same word length as the mystery word.")
	print("The default word length is 5 letters, meaning that your guesses and mystery word will be 5 letters long by default.")

	print("---------------------------------------------------------------")


	print("# OF ATTEMPTS: ")
	print("Determines the amount of guesses you will be able to make before losing the game.")
	print("More attempts makes the game easier, and less attempts makes the game more difficult.")
	print("The default amount of attempts of 6.")

	print("---------------------------------------------------------------")


	print("OBSCURE WORDS: ")
	print("Determines if obscure words are able to be selected as the mystery word.")
	print("Enabling this settings adds obscure words into the pool of mystery word candidates.")
	print("Enabling this setting does not gaurantee that the word you choose will be an obscure word.")
	print("By default, this setting is disabled, meaning that by default only common words can be selected as the mystery word.")

def show_how_to_play():
	print("How to Play: Storts, Chophy, Bascat")
	
	print()
	
	print("Objective: Guess a mystery 5 letter word in 6 attempts.")
	
	print()
	
	print("Each guess must be a valid 5 letter word.")
	print("After each guess, each letter will appear with an associated word that tells you how close your guess was to the mystery word.")
	
	print()

	print("Chophy: Your letter is in the word and is in the correct position.")
	print("Storts: Your letter is in the word, but is not in the correct position.")
	print("Bascat: Your letter does not appear in the word at all.")

	print()

	print("The word length, amount of attempts, and obscure words are settings that can be changed.")
	print("The default settings are 5 letters, 6 attempts, and obscure words are disabled")

	print("-----------------------------------------------------")

	print("EXAMPLE:")

	print()

	print("Mystery Word: WHILE")
	print("Guess: WEARY")

	print()

	print("W: Chophy")
	print("E: Storts")
	print("A: Bascat")
	print("R: Bascat")
	print("Y: Bascat")

def get_words():
	# Adds words to list of guessable words.
	# Picks words from "words_alpha.txt", offering a massive pool of guessable words.
	try:
		with open("assets/words_alpha.txt", "r") as file:
			for word in file:
				# word.strip() function removes \n (New Line Character)
				if len(list(word.strip())) != word_length:
					continue
				guessable_words_list.append(word.strip()) 
	except FileNotFoundError:
		print("No File Exists")

	# Adds words to a separate list.
	# Picks words from "words_10k_most_common.txt", which has a smaller pool than "words_alpha.txt".
	# The mystery word is chosen from this list instead.
	# The purpose of this is to ensure that obscure words are not picked as the mystery word.
	try:
		with open("assets/words_10k_most_common.txt", "r") as file:
			for word in file:
				# word.strip() function removes \n (New Line Character)
				if len(list(word.strip())) != word_length:
					continue
				mystery_word_candiates_list.append(word.strip()) 
	except FileNotFoundError:
		print("No File Exists")

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

# Creates empty list to put words in
mystery_word_candiates_list = []
guessable_words_list = []

# Changeable settings for the game
word_length = 5
attempts = 6
obscure_words = False

# Terminal Colours
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
DEFAULT   = '\033[39m'

if __name__ == "__main__":
	main()