from random import randint

print("Choose 'dam,la,keo':")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "dam"
if computer == 1:
	computer = "la"
if computer == 2:
	computer = "keo"

print("-----")
print("You choose: " + player)
print("computer chooses: " + computer)
print("-----")

if player == computer:
	print("Draw !!")
else:
	if player == "keo":
		if computer == "dam":
			print("You Lose")
		else:
			print("You Win ♥")

	elif player == "dam":
		if computer == "la":
			print("You Lose")
		else:
			print("You Win ♥")

	elif player == "la":
		if computer == "keo":
			print("You Lose")
		else:
			print("You Win ♥")			

	else:
		print("Choose again, Bruh !!!")						
