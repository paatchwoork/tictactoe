from helpers import draw_board
from helpers import evaluate
from helpers import check_turn

import os

import pygame as pg

# Initialize the graphics
pg.init()

screen = pg.display.set_mode((600,800))

# Name of window
pg.display.set_caption('Tic Tac Toe')

# White background
background_color = (255,255,255)
screen.fill(background_color)

# Drawing the board
lines_color = (0,0,0)
# Vertical lines
pg.draw.line(screen, lines_color,(200,0),(200,600),3)
pg.draw.line(screen, lines_color,(400,0),(400,600),3)

# Horizontal lines
pg.draw.line(screen, lines_color,(0,200),(600,200),3)
pg.draw.line(screen, lines_color,(0,400),(600,400),3)

# Set the font
font = pg.font.SysFont('Arial', 40)

# The board in memory
spots={
    1:"1", 2:"2", 3:"3",
    4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9"
    }

turn = 1

running = True

clock = pg.Clock()

# Show the screen
pg.display.flip()

# Run the game
while running :

    # If the payer wants to exit the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()

    # Set the FPS to 30
    clock.tick(30)

    # Player X, your turn
    text = font.render(f'Player {check_turn(turn)[0]}, your turn', True, lines_color, background_color)
    textRect = text.get_rect()
    textRect.center = (300,700)
    screen.blit(text, textRect)
    
    # Check where the mouse is
    check_pos = [0,0]
    if pg.mouse.get_just_pressed()[0]:

        mouse_pos = pg.mouse.get_pos()

        play = 1

        # Adjust the position of the mouse to the center of the square 
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

        # Can't check outside of the board
        if mouse_pos[1] > 600 :
            continue

        # Is the position already checked ?
        if (spots[play] not in ["O","X"]):
            spots[play]=check_turn(turn)[1]
        else :
            continue

        # If all good draw a circle or a cross depending on the player turn
        if spots[play] == "O" :
            # Draw a circle
            pg.draw.circle(screen, lines_color,tuple(check_pos),90,3)
        elif spots[play] == "X" :
            # Draw a cross
            for arm in [(90,90),(-90,-90),(90,-90),(-90,+90)]:
                end = tuple(map(lambda i, j: i + j,check_pos,arm))
                pg.draw.line(screen, lines_color,check_pos,end,3)

        # Evaluate if there is a win or a draw
        if evaluate(spots) == True :
            bigRect = pg.Rect((0,600),(600,200))
            bigRectSurf = pg.Surface((bigRect.w,bigRect.h)) 
            bigRectSurf.fill(background_color)
            screen.blit(bigRectSurf,bigRect)

            text = font.render(f"Player {check_turn(turn)[0]} wins !", True, lines_color, background_color)
            textRect = text.get_rect()
            textRect.center = (300,700)
            screen.blit(text, textRect)
            
            pg.display.flip()

            # Loop until we exit the game
            game_end = True
            while game_end :
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        game_end = False
                        running = False

        elif evaluate(spots) == False :
            
            bigRect = pg.Rect((0,600),(600,200))
            bigRectSurf = pg.Surface((bigRect.w,bigRect.h)) 
            bigRectSurf.fill(background_color)
            screen.blit(bigRectSurf,bigRect)

            text = font.render(f"It's a tie !", True, lines_color, background_color)
            textRect = text.get_rect()
            textRect.center = (300,700)
            screen.blit(text, textRect)
            
            pg.display.flip()

            # Loop until we exit the game
            game_end = True
            while game_end :
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        game_end = False
                        running = False

        turn+=1
