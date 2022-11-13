import numpy as np

from Grid import Board

board = Board(10,10)
board.raise_cell(5,5)
board.raise_cell(5,4)
board.raise_cell(5,3)

print(board.grid)

quitted = False

while not quitted:
    inp = input()
    if inp == "q": quitted = True

    board.step()
    print(board.grid)

    
