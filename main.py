import pygame
import random
import settings as stg
from player import player
from blocks import block


class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((stg.display_width, stg.display_heigh))
        pygame.display.set_caption("Platform")
        self.clock = pygame.time.Clock()
        self.running = True

    def new_game(self):
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(stg.FPS)
            self.events()
            self.update(player)
            self.draw(player, blocks)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_ESCAPE] and self.playing:
            self.playing = False

    def update(self, player):
        player.update()

    def draw(self, player, blocks):
        self.game_display.fill((150, 150, 140))
        for element in blocks:
            element.draw(self.game_display)
        player.draw(self.game_display)
        pygame.display.flip()

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass


game = Game()
game.start_screen()
while game.running:
    player = player(400, 600)
    blocks = [block(200, 500, stg.block_img), block(300, 500, stg.block_img)]
    game.new_game()
    game.game_over_screen()

pygame.quit()
