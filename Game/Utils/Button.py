import pygame, sys


class Button():
    def __init__(self, text, image, size, position, bg_color=None):
        self.text_input = text
        self.image = pygame.image.load(image)
        self.size = size
        self.pos = position
        self.bg_color = bg_color

    def draw(self, surface):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        if self.bg_color != None:
            pygame.draw.rect(surface, self.bg_color, rect)
        self.image = pygame.transform.scale(self.image, self.size)
        surface.blit(self.image, rect)

