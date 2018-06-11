import sys, pygame, time, random, lib
from pygame.locals import *

pygame.init()

#create board
def create_board(board):
    for row in range(board_size): 
        board.append([]) 
        for column in range(board_size): 
            board[row].append(empty_cell) 

#initiate board (for debug purposes)
def initiate_board(board):
    board = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]
    return board
    
#print board to console
def print_board(board):
    x = ["",0,1,2,3,4,5,6,7,8,9]
    print(x)
    i=0
    for row in board:
        print( i, row)
        i+=1

#draw board
def draw_board(board,OFFSET_FROM_TOP,OFFSET_FROM_LEFT,n,size,windowSurface,title,FILL_COLOR,BORDER_COLOR):

    #setup variables
    i = 0
    j = 0

    #set up grid offset
    x = OFFSET_FROM_LEFT
    y = OFFSET_FROM_TOP

    #set up fonts
    basicFont = pygame.font.SysFont('arial', 18)

    # set up the colors
    BLACK = (0, 0, 0)
    GRID_COLOR = (180, 180, 255)
    WHITE = (255,255,255)
    BACKGROUND_COLOR = WHITE

    # set up the block data structure
    blocks = []
    b1 = {'rect':pygame.Rect(x, y, size, size), 'color':FILL_COLOR}
    blocks.append(b1)

    #set up grid lines data structure
    grid = []
    line = []

    x = OFFSET_FROM_LEFT
    y = OFFSET_FROM_TOP
    i = 0
    j = 0
    #
    while(i <= n):
        line = [(x,y),(x,size*n+OFFSET_FROM_TOP)]
        grid.append(line)
        i = i + 1
        x = x+size
        
    x = OFFSET_FROM_LEFT
    y = OFFSET_FROM_TOP
    i = 0
    j = 0
    #   
    while (j <= n):
        line = [(x,y),(size*n+OFFSET_FROM_LEFT,y)]
        grid.append(line)
        j = j + 1
        y = y + size
  

    x = OFFSET_FROM_LEFT
    y = OFFSET_FROM_TOP
    i = 0
    j = 0
    #
    while (i < n):
        while (j < n):
            if board[j][i]==1:
                COLOR = FILL_COLOR
            else: 
                COLOR = BACKGROUND_COLOR
            bij = {'rect':pygame.Rect(x, y, size, size), 'color':COLOR}
            j = j + 1
            y = y + size
            blocks.append(bij)
        x = x + size
        i = i + 1
        j = 0
        y = OFFSET_FROM_TOP
	#end of setup of grid lines 

    #draw custom grid
    i = 0
    j = 0
    x = OFFSET_FROM_LEFT
    y = OFFSET_FROM_TOP
	
    line = []
    grid2 = []

    while(j < n): 
        while(i < n):
            #define color for left cell border
            if (board[i][j] == 1):
                if (j-1 < 0):
                    line = [(x,y),(x,y+size)]
                    grid2.append(line)             
                elif ((board[i][j-1]) != 1):
                    line = [(x,y),(x,y+size)]
                    grid2.append(line)
            
            #define color for top cell border
            if (board[i][j] == 1):
                if (i-1 < 0):
                    line = [(x,y),(x+size,y)]
                    grid2.append(line)
                elif ((board[i-1][j]) != 1):
                    line = [(x,y),(x+size,y)]
                    grid2.append(line)
            
            #define color for right cell border
            if (board[i][j] == 1):
                if (j+1 >= n):
                    line = [(x+size,y),(x+size,y+size)]
                    grid2.append(line)
                elif ((board[i][j+1]) != 1):
                    line = [(x+size,y),(x+size,y+size)]
                    grid2.append(line)

            #define color for bottom cell border
            if (board[i][j] == 1):
                if (i+1 >= n):
                    line = [(x,y+size),(x+size,y+size)]
                    grid2.append(line)                 
                elif((board[i+1][j]) != 1):
                    line = [(x,y+size),(x+size,y+size)]
                    grid2.append(line) 

            i = i + 1
            y = y + size
        j = j + 1
        x = x + size
        i = 0
        y = OFFSET_FROM_TOP

    
    for bij in blocks:
        # draw ships
        pygame.draw.rect(windowSurface, bij['color'], bij['rect'],0)
     
    #draw grid
    for line in grid:
        pygame.draw.line(windowSurface, GRID_COLOR, line[0],line[1],1)
     
    #draw ship borders
    for line in grid2:
       pygame.draw.line(windowSurface, BORDER_COLOR, line[0],line[1],1)

    #draw text
    text = basicFont.render(title, True, BLACK, WHITE)
    textRect = text.get_rect()
    textRect.topleft = (OFFSET_FROM_LEFT,0)
    windowSurface.blit(text, textRect)

    return windowSurface

#pure draw board
def display_boards(windowSurface):
    # run the game loop
    while True:
     # check for the QUIT event
     for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
     pygame.display.update()
     time.sleep(0.02)
             

#print matrix cell value
def print_cell(i,j,board):
    print(i,j,board[i][j])

#calculate number of places for ship
def calc_places (x,n,board):
    #calculate places
    horiz_count = 0
    vert_count = 0
    place_count = 0
    i = 0
    j = 0
    k = 0
    #x = 4
    Places_arr = []
    #Places_arr[0][0] = 0
    cur_place = [0,0,0,0,0]
    #Places_arr = [[],[]]
    
    #find place for a ship: id, start, coords (i,j), direction (horizontal'vertical), length)
    while (i < n):
        while (j < n):
            if (board[i][j]==0):
                horiz_count = 1
                vert_count = 1
                if (j<=n-x):
                    k = 0
                    #check horizontal space
                    while (k < x):
                        if (board[i][j+k] == 0):
                            #horiz_count = horiz_count + 1
                            if (horiz_count == x):
                                place_count = place_count + 1
                                cur_place = list(range(5))
                                cur_place[0] =  place_count
                                cur_place[1] = i
                                cur_place[2] = j
                                cur_place[3] = 1
                                cur_place[4] = x
                                Places_arr.append(cur_place)
                                #print(cur_place)
                            horiz_count = horiz_count + 1
                        k = k +1
                if (i<=n-x):
                    #check vertical space
                    k = 0
                    while (k < x):
                        if (board[i+k][j] == 0):
                            #vert_count = vert_count + 1
                            if (vert_count == x):
                                place_count = place_count + 1
                                cur_place = list(range(5))
                                cur_place[0] =  place_count
                                cur_place[1] = i
                                cur_place[2] = j
                                cur_place[3] = 0
                                cur_place[4] = x
                                Places_arr.append(cur_place)
                                #print(cur_place)
                            vert_count = vert_count + 1
                        k = k +1
            j = j + 1
            k = 0
        i = i + 1
        j = 0
    #print (place_count)
    #select random valid place for a ship
    random.seed()
    place_id = random.randint(1,place_count)
    print(place_id)
    #print(Places_arr)

    #define buffer zone around ship
    #buffer zone: i
    Places_arr[place_id-1].append(Places_arr[place_id-1][1])
    #buffer zone: j
    Places_arr[place_id-1].append(Places_arr[place_id-1][2])
    #buffer zone: horizontal lenght
    Places_arr[place_id-1].append(x+2)
    #buffer zone: vertical length
    Places_arr[place_id-1].append(3)
    #total number of valid places
    Places_arr[place_id-1].append(place_count)
    
    print(Places_arr[place_id-1])
    #check if the found place stick to the top, bottom, left or right edge of the field
    return (Places_arr[place_id-1])

#place ship
def place_ships(place_array, n,board):
    #i coord to place the top left section of the ship
    i = place_array[1]
    #j coord to place the top left section of the ship
    j = place_array[2]
    #ship orientation: 1- horizontal, 0 - vertical
    direction = place_array[3]
    #ship length
    x = place_array[4]
    #i coord of the top left cell of the buffer zone around ship
    buf_i = place_array[5]
    #j coord of the top left cell of the buffer zone around ship
    buf_j = place_array[6]
    #horizontal size of the buffer zone
    horiz_size = place_array[7]
    #vertical size of the buffer zone
    vert_size = place_array[8]
    k = 0
    t = 0

    k = 0
    if (direction == 1):
        #define buffer zone FOR HORIZONTAL SHIP
        #if ship ajusts to the top border
        if (i == 0):
            buf_i = i
            vert_size = 2
        #if ship does not adjust to the top
        else:
            buf_i = i-1
            #if ship adjusts to the bottom
            if (i == n-1):
                vert_size = 2
            #if ship does not adjust to top or bottom
            else:
                vert_size = 3
        #if ship adjusts to the left border
        if (j == 0):
            horiz_size = x+1
            buf_j = j
        else:
            buf_j = j-1
            #if ship adjusts to the right border
            if (j == n-x):
                horiz_size = x+1
            #if ship does not adjust to any border
            else:
                horiz_size = x+2
    else:
        #define buffer zone for VERTICAL ship
        #if ship adjusts to the top
        if (i == 0):
            buf_i = i
            vert_size = x+1
        else:
            buf_i = i-1
            #if ship adjusts to the bottom
            if (i == n-x):
                vert_size = x+1
            #if ship does not adjust to top or bottom
            else:
                vert_size = x+2
        #if ship adjusts to the left edge
        if (j == 0):
            buf_j = j
            horiz_size = 2
        else:
            buf_j = j-1
            #if ship adjust to the right edge
            if (j == n-1):
                horiz_size = 2
            #if ship does not adjust to right or left edge
            else:
                horiz_size = 3

    print(buf_i,buf_j,horiz_size,vert_size)
    
    #i coord to place the top left section of the ship
    i = place_array[1]
    #j coord to place the top left section of the ship
    j = place_array[2]
    
    #fill in buffer zone with '2'
    for k in range(buf_i,buf_i+vert_size,1):
        for t in range(buf_j,buf_j+horiz_size,1):
            board[k][t] = 2
    #if direction is horizontal
    if (direction == 1):
        ship_end_i = i
        ship_end_j = j+x-1
    #if direction is vertical
    else:
        ship_end_i = i+x-1
        ship_end_j = j
        
    #fill in ship zone with '1'
    k = i
    while (k<=ship_end_i):
    #for k in range(i,ship_end_i,1):
        for t in range(j,ship_end_j+1,1):
            board[k][t] = 1
            #print (k,t)
        k+=1

    return board

#investigate loops (for debug)
def loop_print_board(board):
    n = 10
    i = 0
    j = 0
    while(i < n):
        while(j < n):
            print(board[i][j])
            j = j + 1
        #print(i,j)
        i = i + 1
        j = 0   

#prepate text objects
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#draw text
def draw_text(area,message,font,font_size,font_color,x_coord,y_coord):
    text = pygame.font.SysFont(font,font_size)
    textSurf, textRect = lib.text_objects(message, text, font_color)
    textRect.center = (x_coord, y_coord)
    area.blit(textSurf, textRect)
    pygame.display.update()

#draw button
def draw_button (area,button_color,top_left_x,top_left_y,width,heidth,text,font_color):
	pygame.draw.rect(area, button_color,(top_left_x,top_left_y,width,heidth))
	smallText = pygame.font.SysFont("arial",12)
	textSurf, textRect = text_objects(text, smallText, font_color)
	textRect.center = ( (top_left_x+(width/2)), (top_left_y+(heidth/2)) )
	area.blit(textSurf, textRect)
	pygame.display.update()