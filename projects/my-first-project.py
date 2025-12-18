import random

choices = ["rock", "paper", "scissors"]

rounds = 3

user_score = 0
computer_score = 0
round_number = 1

while round_number <= rounds:
    print(f"Round: {round_number}")

    user_choice = input("Choose between rock, paper, or scissors").lower()

    if user_choice not in choices:
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print("It's a tie!!!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("YOU WON THIS ROUND!!!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You Lost This Round!")
        computer_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("YOU WON THIS ROUND!!!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You Lost This Round!")
        computer_score += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("YOU WON THIS ROUND!!!")
        user_score += 1
    elif user_choice == "rock" and computer_choice == "paper":
        print("You Lost This Round!")
        computer_score += 1

    round_number += 1

    print(f"Your final score was: {user_score}")
    print(f"The computers final score was: {computer_score}")
if user_score > computer_score:
    print("YAY!!! YOU ARE THE CHAMPION!!!")
elif user_score == computer_score:
    print("You tied!!!")
else:
    print("Welp, you lost!")