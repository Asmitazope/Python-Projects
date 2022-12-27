# import random library
import random

# initialize user_wins and computer_wins
user_wins = 0
computer_wins = 0

# create option list
options =  [ "rock", "paper", "scissors"]

# looping through options list
while True:
    # convert user input to lower
    user_input = input("Type Rock/Paper/Scissors or Q to Quit:  " ).lower()

    # check if user wants to quit the game
    if user_input == "q":
        break
    
    # if user input is not in options list continue to while loop
    if user_input not in options:
        continue

    # creating a random number between 0 to 2
    random_number = random.randint(0,2)
    # rock=0, paper=1, scissors=2

    # getting random nummber for computer pick
    computer_pick = options[random_number]
    print('\r')
    print("Computer Picked", computer_pick + ".")
    print('\r')

    # if user_input == "rock" and  computer_pick == "scissors" means user won the game
    if user_input == "rock" and  computer_pick == "scissors":

        print("\r You Won The Game :) ")
        print('\r')
        user_wins += 1

    # elif user_input == "rock" and  computer_pick == "scissors" means user won the game 
    elif user_input == "paper" and  computer_pick == "rock":

        print("You Won The Game :) ")
        print('\r')
        user_wins += 1
    
    # if user_input == "rock" and  computer_pick == "scissors" means user won the game
    elif user_input == "scissors" and  computer_pick == "paper":

        print("You Won The Game :) ")
        print('\r')
        user_wins += 1

    # else if none of the above conditions are false means you lost the game/computer won the game
    else:
        print("Computer Won the Game :)" )
        print('\r')
        print("You Lost :( " )
        print('\r')
        computer_wins += 1


print('\r')
print("You Won ", user_wins, "Times")

print('\r')
print("Computer Won", computer_wins, "Times")

print('\r')
print("Thank You For Playing ..")

