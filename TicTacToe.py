import pygame,sys 

pygame.init()
pygame.display.set_caption ( 'Tic Tac Toe')

#create screen 
screen = pygame.display.set_mode((900,900))
screen.fill((0,0,0))

#draws screen lines
def draw_board():

    #horisontal lines
    pygame.draw.line(screen,(255,255,255),(0,300),(900,300),15)
    pygame.draw.line(screen,(255,255,255),(0,600),(900,600),15)
    #vertical lines
    pygame.draw.line(screen,(255,255,255),(300,0),(300,900),15)
    pygame.draw.line(screen,(255,255,255),(600,0),(600,900),15)


draw_board()


#mainloop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pygame.display.update()                