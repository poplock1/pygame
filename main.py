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
        self.all_sprites = pygame.sprite.Group()
        self.player = player(self)
        self.all_sprites.add(self.player)
        self.blocks = pygame.sprite.Group()
        b1 = block(0, 680, 800, 20, stg.block_img)
        b2 = block(20, 480, 60, 20, stg.block_img)
        self.all_sprites.add(b1, b2)
        self.blocks.add(b1, b2)
        self.all_sprites.add(self.blocks)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(stg.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_ESCAPE] and self.playing:
            self.playing = False
            self.running = False

    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            collision = pygame.sprite.spritecollide(self.player, self.blocks, False)
            if collision:
                self.player.pos.y = collision[0].rect.top
                self.player.vel.y = 0

    def draw(self):
        self.game_display.fill((150, 150, 140))
        self.all_sprites.draw(self.game_display)
        pygame.display.flip()

    def start_screen(self):
        pass

    def game_over_screen(self):
        pass


game = Game()
game.start_screen()
while game.running:
    game.new_game()
    game.game_over_screen()

pygame.quit()
