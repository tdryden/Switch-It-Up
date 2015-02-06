# Main calls this class to get the key mapping, up down left right, for the game that is being played
# This could be called in the initialization of a player, and have the keys as attributes of the object
# i.e. player.up, player.down, player.right, player.left = getUp()
# would give the player the keys necessary for moving around.
#

import pygame, random
from pygame.locals import *



arrowkeys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]


def getKey(difficulty):


    if difficulty == 0:
        up = K_UP
        down = K_DOWN
        left = K_LEFT
        right = K_RIGHT

    if difficulty == 1:
        random.shuffle(arrowkeys)
        up = arrowkeys[0]
        down = arrowkeys[1]
        left = arrowkeys[2]
        right = arrowkeys[3]

    if difficulty == 2:


    return up, down, left, right #this is mapped out North south east west