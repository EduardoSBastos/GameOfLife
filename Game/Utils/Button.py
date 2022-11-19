import pygame

class Button():
    def __init__(self, text, image, size, position, bg_color=None):
        self.text_input = text
        self.image = pygame.image.load(image)
        self.size = size
        self.pos = position
        self.bg_color = bg_color
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print ('mouse is over Button')

    def draw(self, surface):
        if self.bg_color != None:
            pygame.draw.rect(surface, self.bg_color, self.rect)
        surface.blit(self.image, self.rect)


