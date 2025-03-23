from helpers import draw_board
from helpers import evaluate
from helpers import check_turn

import os

spots={
    1:"1", 2:"2", 3:"3",
    4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9"
    }

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

turn = 1

while True :
    play = input(f"Player {check_turn(turn)[0]}, your move: ")
    if (str.isdigit(play)) and \
    (int(play) in spots.keys()) and \
    (spots[int(play)] not in ["O","X"]):
        play = int(play)
    else :
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)
        continue
    spots[play]=check_turn(turn)[1]
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if evaluate(spots) == True :
        print (f"Player {check_turn(turn)[0]} wins !")
        break
    elif evaluate(spots) == False :
        print("It's a tie !")
        break
    turn+=1