import pygame, sys


class Button():
    def __init__(self, text, image, size, position):
        self.text_input = text
        self.image = pygame.image.load(image)
        self.size = size
        self.pos = position
        self.color = (0,255,255)

    def draw(self, surface):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(surface, self.color, rect)
        self.image = pygame.transform.scale(self.image, self.size)
        surface.blit(self.image, rect)

