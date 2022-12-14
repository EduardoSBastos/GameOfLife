import sys
import numpy as np
import time
import pygame

from Structure.Game import Game
from GameClasses.Board import Board
from GameClasses.Visual import Visual
from Utils.InputHandler import InputHandler

game = Game()

board = Board(game, (60,60))
board.raise_cell(5,5)
board.raise_cell(6,6)
board.raise_cell(7,4)
board.raise_cell(7,5)
board.raise_cell(7,6)

visual = Visual(game, board, (10,10))

input = InputHandler(game)
input.subToQuitEvent(game.quit_game)

counter = 0
FPS = 60
clock = pygame.time.Clock()
tick = 0.5

while True:
    delta_time = clock.tick(FPS)
    counter += 1 / delta_time
    if counter >= tick:
        game.update()
        counter = 0

