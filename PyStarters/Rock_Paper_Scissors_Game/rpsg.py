import random

print("Winning rules of the game 'Rock Paper Scissors': \n"
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissors wins \n")

while True:
    user_choice = int(input("Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))

    # looping until user enters a valid input
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid choice please: "))

    # initializing value of choice name
    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    else:
        user_choice_name = 'Scissors'

    print('User choice: ' + user_choice_name)

    # computer chooses randomly 
    comp_choice = random.randint(1, 3)

    # initializing values of comp_choice
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    
    print('Computer choice: ' + comp_choice_name)

    print('Who wins: ' + user_choice_name, 'vs', comp_choice_name + '? \n')

    # determine the winner
    if user_choice == comp_choice:
        result = "Draw"
    elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
        result = 'Paper'
    elif (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        result = 'Rock'
    elif (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 2):
        result = 'Scissors'

    # print the result
    if result == 'Draw':
        print("It's a tie!")
    elif result == user_choice_name:
        print("User wins!")
    else:
        print("Computer wins!")

    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

    print('Thanks for playing!')