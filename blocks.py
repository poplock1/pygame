import pygame


block_img = pygame.image.load("grass.png")

class block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def draw(self, gameDisplay):
        gameDisplay.blit(block_img, (self.x, self.y))
