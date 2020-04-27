import random
import logging

randomNumber = random.seed(a=5)
logging.info("Random number generated")

print("User try to guess the random number that was created")
userGuess = input("PLease enter a number:\n")
if userGuess > randomNumber:
    print("Your guess is too high, try again!")
elif userGuess < randomNumber:
    print("Your guess is too low, try again!")
else:
    print("Your guess was spot on. Congradulations, You win!")
