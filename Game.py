#Switch it Up
#Main file


import pygame
from pygame.locals import *

pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
screen = pygame.display.set_mode([700,500])
pygame.display.set_caption("Switch It Up")

#The Implementation of Player class should follow
#class Player(pygame.sprite.Sprite):

class Room(object):
    wall_list = None
    def __int__(self):
        self.wall_list = pygame.sprite.Group()
        
#The Implementation of Wall class should follow
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, fileName):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fileName).convert()

        self.rect = self.image.get_rect()        
        self.rect.x = x
        self.rect.y = y
        
class Room1(Room):
    def __init__(self):
        Room.__init__(self)
        # arbitrary wall coords
        walls = [[0, 0, "block.png"],
                [0, 350,"block.png"],
                [500, 0,"block.png"],
                [500, 350,"block.png"],
                [20, 0,"block.png"],
                [20, 200,"block.png"],
                [390, 350,"block.png"]
                ]
        # add each part of wall to a list
        for thing in walls:
            #wall = Wall(thing[0], thing[1], thing[2], thing[3], thing[4])
            self.wall_list.add(thing)
    
#def getCollision(player,walls): 
    #if pygame.sprite.collide_rect(player,walls):
        
    
    

#main
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            done = True
    screen.fill(WHITE)
    Room1.draw(screen) 
    pygame.display.flip()
    
    
    pygame.quit()
    
    
    
    
