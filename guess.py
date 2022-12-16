# assignment: programming assignment 2
# author: Diwa Ashwini Vittala
# date: 10-26-2020
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import randint

print("Play a game: Guess My Number")
play= "yes"
while play=="yes":
    success= "no"
    mynumber=randint(1,10) #3 while testing
    print("\nYou have three attempts to guess my number.\n")
    for i in range(3):
            if i == 0:
                guessed= int(input("Please enter a number from 1 to 10: "))
            else:
                guessed= int(input("Guess again. Please enter a number: "))
            #after they have entered a number
            if guessed == mynumber:
                success= "yes"
                break
            elif guessed < mynumber:
                print("\nYou guessed wrong. Your number is smaller than mine.\n")
            elif guessed > mynumber:
                print("\nYou guessed wrong. Your number is bigger than mine.\n")
            #at the end of the game, you either won or lost
    if success == "yes":
        print("\nYou guessed right. My number is "+ str(mynumber) +". Congratulations you won!\n")
    else:
        print("\nSorry, you lost. My number is "+ str(mynumber) +".\n")
	#here is to playing again
    play= input("Would you like to play again [Y/N]? ")
    if play.lower() == "y":
        play= "yes"
    else:
        play= "no"

print("\nGoodbye!")
