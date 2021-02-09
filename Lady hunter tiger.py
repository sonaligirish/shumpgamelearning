import random

moves = ['l', 'h', 't']
player_wins = ['lh', 'ht', 'tl']

player_move = input("your move: ")
computer_move = random.choice(moves)

print("you: ", player_move)
print("Me ",computer_move)

if player_move== computer_move:
    print("Tie")
elif player_move + computer_move in player_wins:
    print("You win!")
else:
    print("You lose!")