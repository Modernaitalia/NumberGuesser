import random
import logging

randomNumber = random.randint(1,10)
print(randomNumber)
logging.info("Random number generated")

print("User try to guess the random number that was created")
userGuess = input("Please enter a number:\n")
x = 0
while int(userGuess) != randomNumber:
    if int(userGuess) > randomNumber:
        print("Your guess is too high, try again!")
        continue
        x+=1
    if int(userGuess) < randomNumber:
        print("Your guess is too low, try again!")
        continue
        x+=1

    if int(userGuess) == randomNumber:
        print("Your guess was spot on. Congratulations, You win!")
        break
