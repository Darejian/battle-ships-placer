import sys, pygame, time, random, lib
from pygame.locals import *
pygame.init()

#VARIABLES
boardPlayer1 = [[],[]]
size = 30 #cell size, don't change this
n = 10 # number of cells horizontally/ vertically
running = 1 #1 - keep the game loop running, 0 - stop the game loop

#Color Palette
WHITE = (255,255,255)
PLAYER1_FILL_COLOR = (221,246,221) #light green
#PLAYER1_FILL_COLOR = (221,244,246) #lignt cyan
#PLAYER1_FILL_COLOR = (221,233,246)
PLAYER1_BORDER_COLOR = (103,185,103) #green

BUTTON_COLOR = (0,153,188) #cyan
BUTTON_PRESSED_COLOR = (11,123,151) #darker cyan
FONT_COLOR_NO_HOVER = WHITE 
FONT_COLOR_HOVERED = BUTTON_COLOR

board_size = n #size of the board 
deckShips = [4,3,2,1] #decks which ships can consist of
numberOfShipsPerDeck = [1,2,3,4] # number of ships allowed for appropriate deck (matches with deckShips array)

# set up the window
WINDOWWIDTH = (n*size+2*size)
WINDOWHEIGHT = n*size+2*size + 30
MainWindow = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Battle Ships Placer')

#setup button
b_x = 115 #x coord of the left top corner
b_y = WINDOWHEIGHT - 45 #y coord of the left top corner
b_w = 130 #button width
b_h = 30 #button height


#BODY

# draw the background onto the surface
MainWindow.fill(WHITE)
pygame.display.update()

#draw [Generate] button
lib.draw_button(MainWindow,BUTTON_COLOR,b_x,b_y,b_w,b_h,"Generate New Board",FONT_COLOR_NO_HOVER)
#draw introduction text
intro = ["","","",""]
intro[0] = "Like Buttle Ships game, but tired thinking"
intro[1] = "how to place your ships on the board?"
intro[2] = "This application does it for you!"
intro[3] = "Just press the button!"
smallText = pygame.font.SysFont("arial",15)
i = 0

while (i < 3):
    lib.draw_text(MainWindow, intro[i],"arial",15,FONT_COLOR_HOVERED,WINDOWWIDTH/2,(WINDOWHEIGHT/2 - size + i*25))
    i +=1

#game loop
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
        pygame.quit()
    elif event.type == pygame.MOUSEMOTION:
        print "mouse at (%d, %d)" % event.pos
        mouse = pygame.mouse.get_pos()
        if b_x+b_w > mouse[0] > b_x and b_y+b_h > mouse[1] > b_y:
            lib.draw_button(MainWindow,WHITE,b_x+1,b_y+1,b_w-2,b_h-2,"Generate New Board",FONT_COLOR_HOVERED)
        else:
            lib.draw_button(MainWindow,BUTTON_COLOR,b_x,b_y,b_w,b_h,"Generate New Board",FONT_COLOR_NO_HOVER)
        
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print "PRESSED at (%d, %d)" % event.pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if user clicked the button
        if b_x+b_w > mouse[0] > b_x and b_y+b_h > mouse[1] > b_y:
            #draw pressed button
            lib.draw_button(MainWindow,BUTTON_PRESSED_COLOR,b_x,b_y,b_w,b_h,"Generate New Board",FONT_COLOR_NO_HOVER)
           
    elif event.type == pygame.MOUSEBUTTONUP:
        print "RELEASED at (%d, %d)" % event.pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if user clicked the button
        if b_x+b_w > mouse[0] > b_x and b_y+b_h > mouse[1] > b_y:
            #draw hovered button
            lib.draw_button(MainWindow,WHITE,b_x+1,b_y+1,b_w-2,b_h-2,"Generate New Board",FONT_COLOR_HOVERED)
            
            #initiate board
            boardPlayer1 = lib.initiate_board(boardPlayer1)
            print("Board initiated:")
            lib.print_board(boardPlayer1) #for debug
            #generate new board
            for i in range(0,len(numberOfShipsPerDeck),1):
                for j in range(0,numberOfShipsPerDeck[i],1):
                    ship_place = lib.calc_places (deckShips[i],n,boardPlayer1)
                    boardPlayer1 = lib.place_ships(ship_place,n,boardPlayer1)

                    
            # draw the new board
            MainWindow = lib.draw_board(boardPlayer1,30,30,n,size,MainWindow,"",PLAYER1_FILL_COLOR,PLAYER1_BORDER_COLOR)
        pygame.display.update()
