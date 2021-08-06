import pygame,sys
import arenav0
import numpy as np

clock = pygame.time.Clock()

pygame.init()
WIDTH = 800
HEIGHT = 600
BG_Color = (243,218,178)

offsetx = 20
offsety = 20
edge = 560  #offsetx,offsety,edge

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flipkart GRID 3.0")

data_arena = arenav0.info()
black = (0,0,0)
def arena(x,y,edge,mx,my):      #default ->>20,20,560
    # print(data_arena)
    edge_sq = edge//14
    edge = edge_sq * 14

    light = (255,214,0)
    dark = (245,127,23)
    HoverColorLight = (100, 187, 103)
    HoverColorDark = (76,175,80)

    pygame.draw.rect(screen,light,(x,y,edge,edge))
    
    #Lines
    for _ in range(15):
        xc = x + _ * edge_sq
        pygame.draw.line(screen,black,(xc,y),(xc,y+edge),1)
    for _ in range(15):
        yc = y + _ * edge_sq
        pygame.draw.line(screen,black,(x,yc),(x+edge,yc),1)
    #pits
    for i in range(14):
        for j in range(14):
            if data_arena[i][j] == -1:
                pygame.draw.rect(screen, dark,((x+i*edge_sq),(y+j*edge_sq),edge_sq,edge_sq))
                
            
def hover(mx, my,x,y,edge_sq):
    #HOVER SELECTION
    selected_tile_x = -1
    selected_tile_y = -1
    if((x<mx<x+edge) and (y<my<y+edge)):
        selected_tile_x = (mx - x) // edge_sq
        selected_tile_y = (my - y) // edge_sq

    return selected_tile_x, selected_tile_y


def draw_path(p,x = offsetx,y = offsety,edge = edge):
    edge_sq = edge//14
    edge = edge_sq * 14
    c = edge_sq // 2
    
    if len(p) != 0:
        if len(p) != 1:
            for _ in range(len(p) - 1):
                pygame.draw.line(screen,black,((x + p[_][0]*edge_sq + c),(y + p[_][1]*edge_sq + c)),
                                 ((x + p[_ + 1][0]*edge_sq + c),(y + p[_ + 1][1]*edge_sq + c)),2)
        for _ in range(len(p)):
            pygame.draw.circle(screen,black,((x + p[_][0]*edge_sq + c),(y + p[_][1]*edge_sq + c)),4,0)




'''
Take input from the user and change the path1 to output of the path planning function
'''
### CHANGE THIS LINE \/ \/ \/ \/ \/ \/ 
path1 = [(0,0),(1,0),(2,0),(3,0)] ######
### CHANGE THIS LINE ^^^^^^^^^^^^^^^^^
draw_path_bool = False ### If a path is found then make this variable True







while (draw_path_bool):
    mx, my = pygame.mouse.get_pos()
    
    screen.fill(BG_Color)
    arena(offsetx,offsety,edge, mx, my)
    mxi, myj = hover(mx, my, offsetx, offsety,edge//14)

    
    draw_path(path1)
    

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    
    pygame.display.update()
    clock.tick(144) #easy 144 fps
    # print(int(clock.get_fps()))

