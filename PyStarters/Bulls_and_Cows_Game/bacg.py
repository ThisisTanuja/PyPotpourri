import random

# Generates a 4-digit number with no repeated digits
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num
        
# Returns True if number has no duplicate digits otherwise False
def noDuplicates(num):
    num_li = getDigitList(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
    
# Returns list of digits of a number
def getDigitList(num):
    return [int(i) for i in str(num)]

# returns bulls and cows count
def BullsAndCows(num, guess):
    bulls_and_cows = [0, 0]
    num_list = getDigitList(num)
    guess_list = getDigitList(guess)

    # zip() function returns a zip object, which is an iterator of tuples where the first
    # item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.
    # If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
    for i, j in zip(num_list, guess_list):
        
        # common digit present
        if j in num_list:

            # common digit exact match
            if j == i:
                bulls_and_cows[0] += 1
            # common digit match but in wrong position
            else:
                bulls_and_cows[1] += 1
        
    return bulls_and_cows

# Secret Code 
num = generateNum()
tries = int(input("Enter number of tries: "))

# Play until correct guess or till no tries left
while tries > 0:
    guess = int(input("Enter your guess: "))

    if not noDuplicates(guess):
        print("Number shouldn't have repeated digits")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4-digit number only between 1000" + 'and' + "9999")
        continue

    bulls_and_cows = BullsAndCows(num, guess)

    print(f"{bulls_and_cows[0]} bulls, {bulls_and_cows[1]} cows")
    tries -= 1

    if bulls_and_cows[0] == 4:
        print("You guessed right!")
        break
else: 
    print(f"You ran out of tries. Number was {num}")


