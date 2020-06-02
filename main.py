import pygame
from os import path
import settings as stg
from tile_map import TiledMap
from player import Player
from blocks import block


class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(
            (stg.display_width, stg.display_heigh))
        pygame.display.set_caption("Platform")
        self.game_display_rect = self.game_display.get_rect()
        self.view = self.game_display.get_rect()
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'Maps')
        self.map = TiledMap(path.join(map_folder, 'MAP1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new_game(self):
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.blocks = pygame.sprite.RenderUpdates()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "Player":
                self.player = Player(
                    tile_object.x, tile_object.y, tile_object.width, tile_object.height, self)
                self.all_sprites.add(self.player)
            if tile_object.name == "Ground":
                self.block = block(tile_object.x, tile_object.y,
                                   tile_object.width, tile_object.height)
                self.all_sprites.add(self.block)
                self.blocks.add(self.block)
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
            collision = pygame.sprite.spritecollideany(
                self.player, self.blocks, False)
            if collision:
                self.player.vel.y = 0
                self.player.isJumping = False
                self.player.pos[1] = collision.rect.top + 1
        self.update_view()

    def draw(self):
        map_img = self.map_img
        self.game_display.blit(
            map_img, (0, 0), self.view)
        self.player.draw(map_img)
        pygame.display.update()

    def update_view(self):
        self.view.center = self.player.rect.center
        self.view.clamp_ip(self.map_rect)

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
