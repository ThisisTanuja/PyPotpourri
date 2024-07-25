import random
import math

#taking inputs
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

#total chances to guess the number
total_chances = math.ceil(math.log(upper_bound - lower_bound, 2))
print("\n\t You have only ", total_chances, " chances to guess the number!\n")

#generating a random number between lower and upper bound
random_number = random.randint(lower_bound, upper_bound)

#initializing the number of guesses
count = 0
flag = False


while count < total_chances:
    count += 1

    #taking guessing number as input
    guess = int(input("Guess the number: "))

    #conditions 
    if guess == random_number:
        print("Congratulations! You did it in ", count, " try!")
        flag = True
        break
    elif guess < random_number:
        print("Try Again! You guessed too small!")
    else:
        print("Try Again! You guessed too high!")
        

#if guessing took more than required guesses
if not flag:
    print("\nThe number is %d" % random_number)
    print("Better Luck Next Time!")
