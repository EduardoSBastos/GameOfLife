import sys, pygame

BLACK = 0, 0, 0
WHITE = 255,255,255
GREY = 60,60,60
SCREEN_SIZE = (1280,800)

class Visual:
  def __init__(self, grid_size, cell_size):
    
    self.grid_size = grid_size
    self.cell_size = cell_size
    self.innerScreenSize = (grid_size[0]*cell_size[0], grid_size[1]*cell_size[1])
    pygame.init()
    self.screen = pygame.display.set_mode(self.innerScreenSize)
    self._clear_screen()
    pygame.display.flip()

  def _clear_screen(self):
    self.screen.fill(GREY)
    innerScreenRect = pygame.Rect(0,0, self.innerScreenSize[0], self.innerScreenSize[1])
    pygame.draw.rect(self.screen, BLACK, innerScreenRect)

  def _draw_cell(self, pos):
    rect = pygame.Rect(pos[1]*self.cell_size[1],
                       pos[0]*self.cell_size[0],
                       self.cell_size[1],
                       self.cell_size[0])
    pygame.draw.rect(self.screen, WHITE, rect)
    
  def update(self, grid):
    self._clear_screen()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x,y] == 1:
                self._draw_cell((x,y))
    pygame.display.flip()

