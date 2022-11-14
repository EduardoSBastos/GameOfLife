import sys
import numpy as np
import time
import pygame
from pygame.locals import *

from Grid import Board
from Visual import Visual

board = Board((10,10))
board.raise_cell(5,5)
board.raise_cell(5,4)
board.raise_cell(5,3)

print(board.grid)
visual = Visual(board.size, (15,15))
visual.update(board.grid)

counter = 0
DELTA_TIME = 1/60

while True:
    time.sleep(DELTA_TIME)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER:
                print("Enter")
            if event.type == 768: #Esc
                sys.exit()
            print(event.type)

    counter += 1 * DELTA_TIME
    if counter >= 1:
        board.step()
        visual.update(board.grid)
        counter = 0
    
