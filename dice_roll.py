import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the no. of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid entry, try again.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("\n It's ", player_idx + 1, "player turn")
        print("Your total score is: ", player_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)
        
        player_score[player_idx] += current_score
        print("Your total score is: ", player_score[player_idx])

max_score = max(player_score)
winnig_idx = player_score.index(max_score)
print("Player number", winnig_idx + 1, "is the winner with a score of: ", max_score)
