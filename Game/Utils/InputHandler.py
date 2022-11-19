from events import Events
import pygame
from pygame.locals import *

class InputHandler:
    def __init__(self):
        self.events = Events()
    
    def subToQuitEvent(self, objMethod):
        self.events.onQuit += objMethod

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.events.onQuit()
            if event.type == KEYDOWN:
                if event.type == 768: #Esc
                    self.events.onQuit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)