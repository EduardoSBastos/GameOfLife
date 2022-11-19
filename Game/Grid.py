import numpy as np

class Board:
  def __init__(self, size, square_size=10):
    self.size = size
    self.width = size[1]
    self.height = size[0]
    self. grid = np.zeros(self.size).astype(int)


  def step(self):
    next_grid = np.zeros(self.size).astype(int)
    for x in range(self.width):
        for y in range(self.height):
            next_grid[y,x] = self._next_step_status(y,x)
    self.grid = next_grid

  def show_neighbours(self):
    neighbour_grid = np.zeros(self.size).astype(int)
    for x in range(self.width):
        for y in range(self.height):
            neighbour_grid[x,y] = self._count_living_neighbours(x,y)
    print(neighbour_grid)


  def raise_cell(self, x:int, y:int):
    if x<0 or x >=self.width or y<0 or y >=self.height:
        print('Error: cell out of bounds!!')
        return False
    self.grid[x,y] = 1
    return True


  def _next_step_status(self, x:int, y:int):
    num_neighbours = self._count_living_neighbours(x,y)
    if num_neighbours == 3:
        return 1
    if self._cell_status(x,y) == 1:
        if num_neighbours == 2 or num_neighbours == 3:
            return 1
    return 0
  

  def _count_living_neighbours(self, x:int, y:int):
    return ( self._cell_status(x-1,y-1) + self._cell_status(x,y-1) + self._cell_status(x+1,y-1)
           + self._cell_status(x-1,y)                              + self._cell_status(x+1,y)
           + self._cell_status(x-1,y+1) + self._cell_status(x,y+1) + self._cell_status(x+1,y+1))
    

  def _cell_status(self, x:int, y:int):
    if x<0 or x>=self.height or y<0 or y>=self.width:
        return 0
    return self.grid[x,y]