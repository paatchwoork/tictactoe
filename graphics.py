import pygame as pg

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

# check_pos = (100,100)

# # Draw a cross
# for arm in [(90,90),(-90,-90),(90,-90),(-90,+90)]:
#     print(arm)
#     end = tuple(map(lambda i, j: i + j,check_pos,arm))
#     pg.draw.line(screen, lines_color,check_pos,end,3)

# # Draw a circle
# pg.draw.circle(screen, lines_color,check_pos,90,3)


running = True

clock = pg.Clock()

while running :

    check_pos = [0,0]
    if pg.mouse.get_pressed()[0]:

        mouse_pos = pg.mouse.get_pos()

        if mouse_pos[0] > 0 and mouse_pos[0] < 200 :
            check_pos[0] = 100
        if mouse_pos[1] > 0 and mouse_pos[1] < 200 :
            check_pos[1] = 100

        if mouse_pos[0] > 200 and mouse_pos[0] < 400 :
            check_pos[0] = 300
        if mouse_pos[1] > 200 and mouse_pos[1] < 400 :
            check_pos[1] = 300

        if mouse_pos[0] > 400 and mouse_pos[0] < 600 :
            check_pos[0] = 500
        if mouse_pos[1] > 400 and mouse_pos[1] < 600 :
            check_pos[1] = 500

        print(mouse_pos, check_pos)

        # Draw a circle
        pg.draw.circle(screen, lines_color,tuple(check_pos),90,3)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(30)
    pg.display.flip()

pg.quit()