# Bulls and Cows Game

# Task
+ This is a pen and paper code-breaking game usually played betweeen 2 players . 
+ A player tries to guess a secret code number chosen by the second player.
+ The rules are:
 + A player will create a secret code, usually a 4-digit number. This number should have no repeated digits.
 + Another player makes a guess to crack the secret number. Upon making a guess, 2 hints will be provided - Cows and Bulls.
 + Bulls indicate the number of correct digits in the correct position and cows indicates the number of correct digits in the wrong position. 
 + The player keeps on guessing until the secret code is cracked . The player who guesses in the minimum number of tries wins.

# Output
+ If the secret code is 1234 and the guesses number is 1246 then we have 2 BULLS(for the exact matches of digits 1 and 2) and 1 COW (for the match of digit 4 in the wrong position)

# Constraint
+ The secret code and the guessed code should be of 4 digits between 1000 and 9999 and have no repeated numbers.
