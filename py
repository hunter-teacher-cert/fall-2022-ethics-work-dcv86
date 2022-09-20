import random

stones = 12
stonesTaken = 0
player = ("Human")
print ("Stones = ", stones)
while (stones > 0):
	if(player=="Human" and stones >= 3):
		print("How many stones would you like 1, 2 or 3?")
		stonesTaken=int(input())			
		while(stonesTaken > 3 or stonesTaken < 1):
			print ("Woops! Please select 1, 2 or 3 only!")
			stonesTaken=int(input())
		player = "Human"
		stones = stones - stonesTaken
		print("\nStones left: ", stones)
		
		if (player=="Human" and stones == 2):
			print("How many stones would you like 1 or 2?")
			stonesTaken=int(input())			
			while(stonesTaken > 2 or stonesTaken < 1):
				print ("Woops! Please select 1 or 2 only!")
				stonesTaken=int(input())
			player = "Human"
			stones = stones - stonesTaken
			print("\nStones left: ", stones)
			if (stones < 1):
				break
			
	player = "computer"
	
	if(player=="computer" and stones >= 3):
		stonesTaken = random.randint(1,3)
		print("\nThe computer takes", stonesTaken," stones.")
		stones = stones - stonesTaken
		print("\nStones left: ", stones)
		if (stones < 1):
			break
		player = "human"
	

	if(player=="computer" and (stones == 2 or stones == 1)):
		stonesTaken = random.randint(1,2)
		print("The computer takes", stonesTaken," stones.")
		stones = stones - stonesTaken
		print("Stones left: ", stones)
		
		if (stones < 1):
			break
	player = "Human"

	if(player=="computer" and stones == 1):
		stonesTaken = 1
		print("The computer takes", stonesTaken, " stones.")
		stones = stones - stonesTaken
		print("Stones left: ", stones,)
		if (stones < 1):
			break
	player = "Human"
print ("the ", player, " wins!")
