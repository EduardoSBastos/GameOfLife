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
    self.initialize_screen(self.innerScreenSize)


  def initialize_screen(self, innerScreenSize):
    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    self.screen.fill(GREY)
    innerScreenRect = pygame.Rect(30,30, 30+innerScreenSize[0], 30+innerScreenSize[1])
    pygame.draw.rect(self.screen, BLACK, innerScreenRect)
    pygame.display.flip()


  def update(self, grid):
    self.screen.fill(GREY)
    pygame.draw.rect(self.screen, WHITE, pygame.Rect(30,30,60,60))
    pygame.display.flip()
