import random  #import a random package

choices = ["stone", "paper","scissors"]

while True: #there no condition to stop the code
    user_choice = input("Enter stone,paper, or scissors (or 'quit' to stop): ").lower()
    # lower is an function and it will convert the inputs into lower case incase of we put the upper case input it will automatically convert into lower case
    if user_choice == "quit": # if the function can compare the quit means Game will be Over
        print("Game Over!")
        break # it will break the while condition

    computer_choice = random.choice(choices)
    # random is package and  inside the package choices to take anything from the given list for play the game
    print(f"Computer chose: {computer_choice}")
    # f refers to the FORMATTING  the output

    if user_choice == computer_choice:
        print("It is Tie!")
    elif ( user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")

    else:
        print("you lose!")







