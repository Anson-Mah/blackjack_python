# Pseudo-Blackjack

import random
import time

money=100
global rounds
rounds=0

while money>0:
	
	def play(): 
		
		global money
		
		bet_status=bool(False)
		attempts=0
		
		while bet_status==bool(False):
			if attempts==0:
				bet=int(input("Your Bet: $"))
			else: 
				bet=int(input("Your New Bet: $"))
			print(" ")
			if bet>money:
				print("You cannot bet more than you have.")
				attempts+=1
				print(" ")
			elif bet<0:
				print("You cannot bet negative money.")
				attempts+=1
				print(" ")
			else: 
				bet_status=bool(True)
	
		cards=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
		player_number=random.choice(cards)
		arbitrary_value=0
		
		print(f"Your Current Number: {player_number}")
		
		while arbitrary_value<1:
			option=input("Hit (H) or Stand (S)?: ")
			if option=="H" or option=="h": 
				print(" ")
				random_card=random.choice(cards)
				player_number+=random_card
				print(f"Card Drawn: {random_card}")
				print(f"Your Current Number: {player_number}")
				print(" ")
				if player_number>21: 
					print("You busted. You lose.")
					print(" ")
					time.sleep(1)
					print(f"Change in Balance: -${bet}")
					money-=bet
					arbitrary_value+=2
			elif option=="S" or option=="s": 
				arbitrary_value+=1
			else: 
				print("Your input was not recognized. Please input again.")
		
		if arbitrary_value==1: 
			dealers_number=random.choice(cards)
			print(" ")
			print(f"Dealer's Current Number: {dealers_number}")
			time.sleep(1)
			while dealers_number<17: 
				random_card=random.choice(cards)
				print(" ")
				print(f"Card Drawn: {random_card}")
				dealers_number+=random_card
				print(f"Dealer's Current Number: {dealers_number}")
				#print(" ")
				time.sleep(1)
			print(" ")
			if dealers_number>21:
				print("Dealer busted. You win!")
				print(" ")
				time.sleep(1)
				print(f"Change in Balance: ${bet}")
				money+=bet
			elif dealers_number>player_number: 
				print("Dealer has higher number than you. You lose this round.")
				print(" ")
				time.sleep(1)
				print(f"Change in Balance: -${bet}")
				money-=bet
			elif dealers_number==player_number: 
				print("You and dealer have the same number. This round is a tie.")
				print(" ")
				time.sleep(1)
				print(f"Change in Balance: $0")
			else:
				print("You have higher number than dealer. You win this round!.")
				print(" ")
				time.sleep(1)
				print(f"Change in Balance: ${bet}")
				money+=bet
	
	if rounds>0:
		time.sleep(1)
		print(" ")
		print(f"Your New Balance: ${money}")
		time.sleep(1)
	else: 
		print("Your Balance: $100")
		rounds+=1
	print(" ")
	play()

print(f"Your New Balance: ${money}")
print(" ")
print("You have no money left. You have been kicked out of the casino.")
