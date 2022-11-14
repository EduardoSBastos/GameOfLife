import numpy as np

from Grid import Board
from Visual import Visual

board = Board((10,10))
board.raise_cell(5,5)
board.raise_cell(5,4)
board.raise_cell(5,3)

print(board.grid)
visual = Visual(board.size, (10,10))
visual.update(board.grid)
    
quitted = False
while not quitted:
    inp = input()
    if inp == "q":
        quitted = True
        continue

    board.step()
    visual.update(board.grid)
    print(board.grid)
    
