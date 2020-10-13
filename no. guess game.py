import random

number = random.randint(1, 50)
chances = 0

print("Guess a number (between 1 and 50):")

while chances < 10:
	guess = int( input("Enter Your Guess: "))
	if guess == number:
		print("Congratulation YOU WON!!!")
		exit()
	elif guess < number:
		print("Your guess was too low")
	else:
		print("Your guess was too high")
	chances += 1
	print("Chances Left : ",10-chances)

print( "YOU LOSE!!! The number is : ", number)
