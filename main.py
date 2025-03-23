from helpers import draw_board
from helpers import evaluate
from helpers import check_turn

import os

import pygame as pg


# Initialize the graphics
pg.init()

screen = pg.display.set_mode((600,600))

# White background
background_color = (255,255,255)
screen.fill(background_color)

# Drawing the board
lines_color = (0,0,0)
# Vertical lines
pg.draw.line(screen, lines_color,(200,0),(200,600),3)
pg.draw.line(screen, lines_color,(400,0),(400,600),3)

#Horizontal lines
pg.draw.line(screen, lines_color,(0,200),(600,200),3)
pg.draw.line(screen, lines_color,(0,400),(600,400),3)


# The board
spots={
    1:"1", 2:"2", 3:"3",
    4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9"
    }

# Clear the screen and draw the board
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

turn = 1

running = True

clock = pg.Clock()

# Run the game
while running :

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(30)
    pg.display.flip()

    # Ask the user to play
    # play = input(f"Player {check_turn(turn)[0]}, your move: ")
    check_pos = [0,0]
    if pg.mouse.get_just_pressed()[0]:

        mouse_pos = pg.mouse.get_pos()

        play = 1

        if mouse_pos[0] > 0 and mouse_pos[0] < 200 :
            check_pos[0] = 100
            play += 0
        if mouse_pos[1] > 0 and mouse_pos[1] < 200 :
            check_pos[1] = 100
            play += 0

        if mouse_pos[0] > 200 and mouse_pos[0] < 400 :
            check_pos[0] = 300
            play += 1
        if mouse_pos[1] > 200 and mouse_pos[1] < 400 :
            check_pos[1] = 300
            play+=3

        if mouse_pos[0] > 400 and mouse_pos[0] < 600 :
            check_pos[0] = 500
            play += 2
        if mouse_pos[1] > 400 and mouse_pos[1] < 600 :
            check_pos[1] = 500
            play+=6

        spots[play]=check_turn(turn)[1]
        print(check_turn(turn)[0])
        print(check_turn(turn)[1])
        if spots[play] == "O" :
            # Draw a circle
            pg.draw.circle(screen, lines_color,tuple(check_pos),90,3)
        elif spots[play] == "X" :
            # Draw a cross
            for arm in [(90,90),(-90,-90),(90,-90),(-90,+90)]:
                print(arm)
                end = tuple(map(lambda i, j: i + j,check_pos,arm))
                pg.draw.line(screen, lines_color,check_pos,end,3)

        # os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)

        # Evaluate if ther is a win or a draw
        if evaluate(spots) == True :
            print (f"Player {check_turn(turn)[0]} wins !")
            # break
        elif evaluate(spots) == False :
            print("It's a tie !")
            # break

        turn+=1

    # # Checks if the input is right
    # if (str.isdigit(play)) and \
    # (int(play) in spots.keys()) and \
    # (spots[int(play)] not in ["O","X"]):
    #     play = int(play)
    # else :
    #     # os.system('cls' if os.name == 'nt' else 'clear')
    #     # draw_board(spots)
    #     continue
    
    # If it is, put a check at the corresponding location
    # spots[play]=check_turn(turn)[1]
    # os.system('cls' if os.name == 'nt' else 'clear')
    # draw_board(spots)

    # Evaluate if ther is a win or a draw
    # if evaluate(spots) == True :
    #     print (f"Player {check_turn(turn)[0]} wins !")
    #     break
    # elif evaluate(spots) == False :
    #     print("It's a tie !")
    #     break
    # turn+=1