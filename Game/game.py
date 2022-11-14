import sys
import numpy as np
import time
import pygame

from Grid import Board
from Visual import Visual
from InputHandler import InputHandler

board = Board((10,10))
board.raise_cell(5,5)
board.raise_cell(5,4)
board.raise_cell(5,3)

visual = Visual(board.size, (15,15))
visual.update(board.grid)

counter = 0
DELTA_TIME = 1/60

class Quitter():
    def quit_game(self):
        sys.exit()

input = InputHandler()
input.subToQuitEvent(Quitter().quit_game)

while True:
    time.sleep(DELTA_TIME)
    input.update()

    counter += 1 * DELTA_TIME
    if counter >= 1:
        board.step()
        visual.update(board.grid)
        counter = 0

    
