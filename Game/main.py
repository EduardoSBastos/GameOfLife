import sys
import numpy as np
import time
import pygame

from Structure.Game import Game
from GameClasses.Grid import Board
from Visual import Visual
from Utils.InputHandler import InputHandler

game = Game()

board = Board(game, (10,10))
board.raise_cell(5,5)
board.raise_cell(5,4)
board.raise_cell(5,3)

visual = Visual(board.size, (15,15))
visual.update(board.grid)

counter = 0
FPS = 60
clock = pygame.time.Clock()

class Quitter():
    def quit_game(self):
        sys.exit()

input = InputHandler()
input.subToQuitEvent(Quitter().quit_game)

while True:
    delta_time = clock.tick(FPS)
    input.update()
    counter += 1 / delta_time
    if counter >= 1:
        game.update()
        visual.update(board.grid)
        counter = 0

