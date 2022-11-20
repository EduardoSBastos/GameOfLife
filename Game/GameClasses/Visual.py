import sys, pygame
from Structure.GameObj import GameObj
from GameClasses.Board import Board

BLACK = 0, 0, 0
WHITE = 255,255,255
GREY = 60,60,60
SCREEN_SIZE = (1280,800)

class Visual(GameObj):
  def __init__(self, game, board:Board, cell_size):
    self.board = board
    self.grid_size = board.size
    self.cell_size = cell_size
    self.innerScreenSize = (self.grid_size[0]*cell_size[0], self.grid_size[1]*cell_size[1])
    pygame.init()
    self.screen = pygame.display.set_mode(self.innerScreenSize)
    self._clear_screen()
    pygame.display.flip()
    super().__init__(game)

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
    
  def update(self):
    grid = self.board.grid
    self._clear_screen()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x,y] == 1:
                self._draw_cell((x,y))
    pygame.display.flip()

