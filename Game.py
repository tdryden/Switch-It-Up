#Switch it Up
#Main file


import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([700,500])
pygame.display.set_caption("Switch It Up")

x_Dragon = 0;
y_Dragon = 0;
#The Implementation of Player class should follow
class Player(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(filename).convert()
        
        # set the rectangle defined for this image for collision detection
        self.rect = self.image.get_rect()
        # position the image
        #self.Reset(self)
        
        self.rect.x_Dragon = 350
        self.rect.y_Dragon = 250
        
        # sets the lives to three
        self.lives = 3;
    
    def getNumLives(self):
        return self.lives
    
    #Checks if the dragon is colliding with the wall
    def getCollision(self, wall2):
        global x_Dragon
        global y_Dragon
        
        if pygame.sprite.collide_rect(self, block2):
            
            x_Dragon = random.randrange(700 - self.rect.width)
            
            y_Dragon = random.randrange(500 - self.rect.height)
    def moveDown(self):
        global y_Dragon
        y_Dragon = y_Dragon - 2
    
    def moveUp(self):
        global y_Dragon
        y_Dragon = y_Dragon + 2
    
    def moveLeft(self):
        global x_Dragon
        x_Dragon = x_Dragon -2
        
    def moveRight(self):
        global x_Dragon
        x_Dragon = x_Dragon +2
        
state = 0
while state != 1:
                
        
        
        
        
        
        
        
        


    