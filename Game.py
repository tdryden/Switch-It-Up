#Switch it Up
#Main file


import pygame
from pygame.locals import *

pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
screen = pygame.display.set_mode([700,500])
pygame.display.set_caption("Switch It Up")


        
#The Implementation of Wall class should follow
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()        
        self.rect.x = x
        self.rect.y = y
        

wall_list = pygame.sprite.Group()
walls = [[0, 0, 20, 1, BLACK],
        [0, 350, 20, 1, BLACK],
        [500, 0, 20, 1, BLACK],
        [500, 350, 20, 1, BLACK],
        [20, 0, 20, 1, BLACK],
        [20, 200, 20, 1, BLACK],
        [390, 350, 20, 1, BLACK]
        ]
        # add each part of wall to a list
for thing in walls:
    wall = Wall(thing[0], thing[1], thing[2], thing[3], thing[4])
    wall_list.add(wall)

#main
clock = pygame.time.Clock()
done = False
while not done:
    screen.fill(WHITE)

    wall_list.draw(screen) 
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    clock.tick(30)
    
pygame.quit()
    
    
    
    
