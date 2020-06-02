import pygame
from os import path
# Game options
display_width = 1280
display_heigh = 720
level_width = 1200
level_heigh = 700
FPS = 60
# Player properties
player_acc = 1
player_friction = -0.2
# Player images
game_dir = path.dirname(__file__)
player_sprites = path.join(game_dir, 'Base pack/Player')

walkRight = [pygame.image.load(path.join(player_sprites, 'p1_walk/PNG/p1_walk01.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk02.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk03.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk04.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk05.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk06.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk07.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk08.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk09.png')),
             pygame.image.load(
                 path.join(player_sprites, 'p1_walk/PNG/p1_walk10.png')),
             pygame.image.load(path.join(player_sprites, 'p1_walk/PNG/p1_walk11.png'))]

jumpRight = pygame.image.load(
    path.join(player_sprites, 'p1_jump.png'))
jumpLeft = pygame.transform.flip(jumpRight, 1, 0)

walkLeft = []

for element in walkRight:
    new_element = pygame.transform.flip(element, 1, 0)
    walkLeft.append(new_element)

stand_still = pygame.image.load(
    path.join(player_sprites, 'p1_front.png'))
