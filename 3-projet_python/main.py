# 3 PIG GAME 

import random

#  generate a random roll 
def Roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value , max_value)
    # return random.randint(min_value , max_value)
    return roll
#  tester la foction
# value = Roll()
# print("Player 1 Turn" , value)

while True:
    players = input("Enter the number of players (2-4) :")
#  check if the number is valid
    if players.isdigit():
        players = int(players)
        if players <= 4 and players >= 2:
            break

        else:
            print("Must be between 2 - 4 players.")
    else : 
        print ("Invalid entry! Please try again.")

max_score = 50
# we will make a list of comparasion for eacht player
player_scores = [ 0 for _ in range(players)]
#  tester the list of comparasion
# print(player_scores)

#  now, we need to go through our player terms
while max(player_scores) < max_score:

    for player_idx in range(players):

        print(f"\n player number {player_idx+1} has started ")
        print(" Your total score is" , player_scores[player_idx], "\n")
        current_value = 0

        while True:

            should_roll = input("would you like to roll (y)")

            if should_roll.lower() != 'y':
                break

            value = Roll()
            
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_value = 0
                break
            
            else:
                current_value += value  
                print("You rolled a:", value)

            print("your score is , " ,current_value)

        player_scores[player_idx] += current_value

        print("your score is , " ,player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"\nGame over! player number {winning_idx +1 } is the winner with a score of : {max_score}")
