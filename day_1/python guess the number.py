import random

number = random.randint( 1,100)
# we can assign the condition for a number is 1 to 100
# RANDINT can generate the number 1 to 100
print("Guess the number between 1 to 100")

while True:
    guess = int(input("Enter your guess:"))
    if guess < number :
        print("Too low!")
    elif guess > number :
        print("Too high!")

    else:
        print("Congratulations! You guessed it...")
        break