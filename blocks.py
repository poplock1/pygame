import pygame


block_img = pygame.image.load("grass.png")


class block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = block_img
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y

    # def draw(self, game_display):
    #     game_display.blit(block_img, (self.x, self.y))
    #     self.rect = self.image.get_rect(topleft=(self.x, self.y))
    #     pygame.draw.rect(game_display, (0, 255, 0), self.rect, 2)
