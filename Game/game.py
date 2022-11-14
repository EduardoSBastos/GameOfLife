import numpy as np
import time

from Grid import Board
from Visual import Visual

board = Board((10,10))
board.raise_cell(5,5)
board.raise_cell(5,4)
board.raise_cell(5,3)

print(board.grid)
visual = Visual(board.size, (15,15))
visual.update(board.grid)
    
quitted = False
while True:
    time.sleep(0.8)

    board.step()
    visual.update(board.grid)
    print(board.grid)
    
