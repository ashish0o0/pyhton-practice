import random

user_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick, ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins+1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "scissor":
        print("It's a draw")
    elif user_input == "paper" and computer_pick == "paper":
        print("It's a draw")
    elif user_input == "rock" and computer_pick == "rock":
        print("It's a draw")
    else:
        print("You lost!")
        computer_wins += 1

    print("score (", user_wins, ":", computer_wins, ")")

if user_wins > computer_wins:
    print("You won")
elif user_wins < computer_wins:
    print("The computer won")
else:
    print("It's a draw")
