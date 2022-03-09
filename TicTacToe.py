import pygame,sys 
import numpy as np

pygame.init()
pygame.display.set_caption ( 'Tic Tac Toe')

#create screen 
screen = pygame.display.set_mode((900,900))
screen.fill((0,0,0))

#create board

board =np.zeros((3,3))
print(board)

#draws screen lines
def draw_screen_lines():

    #horisontal lines
    pygame.draw.line(screen,(255,255,255),(0,300),(900,300),15)
    pygame.draw.line(screen,(255,255,255),(0,600),(900,600),15)
    #vertical lines
    pygame.draw.line(screen,(255,255,255),(300,0),(300,900),15)
    pygame.draw.line(screen,(255,255,255),(600,0),(600,900),15)


#marks board square
def place_square(row,col,player):
    board[row][col] = player


#returns if square is available
def available_square(row,col):
    return board[row][col]==0


#checks if board is full
def is_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True


#links numerical board with screen board and marks square for each player respectively
def draw_player_markers(): # X or O
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen,(124,252,0),(col * 300 +50,row * 300 + 250),(col*300+250,row *300 +50),25)
                pygame.draw.line(screen,(124,252,0),(col * 300 +50,row * 300 + 50),(col*300+250,row *300 +250),25)
            elif board[row][col] == 2:
                 pygame.draw.circle(screen,(255,0,0),(int(col * 300 + 150),int(row * 300 + 150)),110,25)
                
        
draw_screen_lines()
player =1

#mainloop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        #check if player picked a square and stores its coordinates
        if event.type == pygame.MOUSEBUTTONDOWN:
            X = event.pos[0]
            Y = event.pos[1]
            #rounding up coordinates to get board row and col
            selected_row = int(Y // 300)
            selected_col = int(X // 300)

            #places player marker and alternates between the two players
            if available_square(selected_row,selected_col):
                if player == 1:
                    place_square(selected_row,selected_col,1)
                    player=2
                elif player == 2:
                    place_square(selected_row,selected_col,2)   
                    player = 1 

                draw_player_markers()

    pygame.display.update()                