from events import Events
import pygame
from pygame.locals import *
from Structure.GameObj import GameObj

class InputHandler(GameObj):
    def __init__(self, game):
        self.events = Events()
        super().__init__(game)
    
    def subToQuitEvent(self, objMethod):
        self.events.onQuit += objMethod

    def update(self):
        for event in pygame .event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.QUIT:
                        self.events.onQuit()
                    case pygame.K_ESCAPE:
                        self.events.onQuit()
                    case pygame.K_SPACE:
                        self.events.onPauseButton()
                        print('Pause pressed')
                    case _:
                        continue
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.events.onLeftMouseClick(pos)
                print(pos)
            