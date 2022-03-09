import pygame
import sys
import numpy as np

pygame.init()
pygame.display.set_caption('Tic Tac Toe')

# create screen
screen = pygame.display.set_mode((900, 900))
screen.fill((0, 0, 0))


# create board
board = np.zeros((3, 3))
print(board)


# draws screen lines
def draw_screen_lines():
    # horisontal lines
    pygame.draw.line(screen, (255,0,255), (0, 300), (900, 300), 15)
    pygame.draw.line(screen, (255,0,255), (0, 600), (900, 600), 15)
    # vertical lines
    pygame.draw.line(screen, (255,0,255), (300, 0), (300, 900), 15)
    pygame.draw.line(screen, (255,0,255), (600, 0), (600, 900), 15)


# marks board square
def place_square(row, col, player):
    board[row][col] = player


# returns if square is available
def available_square(row, col):
    return board[row][col] == 0


# checks if board is full
def is_full():
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return False
    return True


# links numerical board with screen board and marks square for each player respectively
def draw_player_markers():  # X or O
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                pygame.draw.line(screen, (124, 252, 0), (col * 300 + 50,row * 300 + 250), (col*300+250, row * 300 + 50), 25)
                pygame.draw.line(screen, (124, 252, 0), (col * 300 + 50,row * 300 + 50), (col*300+250, row * 300 + 250), 25)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, (255, 0, 0), (int(
                    col * 300 + 150), int(row * 300 + 150)), 110, 25)


#checks if player move wins the game
def check_win(player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_winning_lines(player, 'vertical', col)
            return True

    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_winning_lines(player, 'horisontal', row)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_winning_lines(player, 'primaryDiagonal', -1)
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_winning_lines(player, 'secondaryDiagonal', -1)
        return True

    return False


#draws the winning squares
def draw_winning_lines(player, type, row_col):
    if player == 1:
        color = (124, 252, 0)
    elif player == 2:
        color = (255, 0, 0)

    if type == 'horisontal':
        pygame.draw.line(screen, color, (15, row_col*300+150), (900-15, row_col*300+150), 15)
    elif type == 'vertical':
        pygame.draw.line(screen, color, (row_col*300+150, 15),(row_col*300+150, 900-15), 15)
    elif type == 'primaryDiagonal':
        pygame.draw.line(screen, color, (15, 15), (900-15, 900-15), 15)
    elif type == 'secondaryDiagonal':
        pygame.draw.line(screen, color, (15, 900-15), (900-15, 15), 15)


#initializes the game
def restart_game():
    screen.fill((0, 0, 0))
    draw_screen_lines()
    for row in range(len(board)):
        for col in range(len(board)):
            board[row][col] = 0


draw_screen_lines()
player = 1
game_finished = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # check if player picked a square and stores its coordinates
        if event.type == pygame.MOUSEBUTTONDOWN and not game_finished:
            X = event.pos[0]
            Y = event.pos[1]
            # rounding up coordinates to get board row and col
            selected_row = int(Y // 300)
            selected_col = int(X // 300)

            # places player marker and alternates between the two players
            if available_square(selected_row, selected_col):
                if player == 1:
                    place_square(selected_row, selected_col, 1)
                    if check_win(player):
                        game_finished = True
                    player = 2
                elif player == 2:
                    place_square(selected_row, selected_col, 2)
                    if check_win(player):
                        game_finished = True
                    player = 1

                draw_player_markers()
        #when u press 'r' the game restarts
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_finished = False
                player = 1

    pygame.display.update()