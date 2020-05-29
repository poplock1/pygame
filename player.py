import pygame
import settings as stg

vec = pygame.math.Vector2

walkRight = [pygame.image.load("player_sprite/p1_walk/PNG/p1_walk01.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk02.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk03.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk04.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk05.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk06.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk07.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk08.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk09.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk10.png"),
             pygame.image.load("player_sprite/p1_walk/PNG/p1_walk11.png")]
jumpRight = pygame.image.load("player_sprite/p1_jump.png")

walkLeft = []
jumpLeft = pygame.transform.flip(pygame.image.load("player_sprite/p1_jump.png"), 1, 0)

for element in walkRight:
    new_element = pygame.transform.flip(element, 1, 0)
    walkLeft.append(new_element)

stand_still = pygame.image.load("player_sprite/p1_front.png")


class player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = stand_still
        self.rect = self.image.get_rect()
        self.rect.center = (stg.display_width / 2, stg.display_heigh - 195)
        self.pos = vec(stg.display_width / 2, stg.display_heigh - 195)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.game = game
        self.left = False
        self.right = False
        self.walkCount = 0

    def jump(self):
        self.rect.x += 1
        collision = pygame.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.x -= 1
        if collision:
            self.vel.y = -12

    def update(self):
        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.pos.x > (self.rect.size[0]/2):
            self.acc.x = -stg.player_acc
            self.right = False
            self.left = True
        elif keys[pygame.K_RIGHT] and self.pos.x <= (stg.display_width - 3*(self.rect.size[0]/2)):
            self.acc.x = stg.player_acc
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0
    
        self.acc.x += self.vel.x * stg.player_friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    # def draw(self, game_display):
    #     if self.walkCount + 1 >= 33:
    #         self.walkCount = 0
    #     if self.right:
    #         if self.isJumping:
    #             game_display.blit(jumpRight, (self.pos.x, self.pos.y))
    #         else:
    #             game_display.blit(walkRight[self.walkCount//3], (self.pos.x, self.pos.y))
    #             self.walkCount += 1
    #     elif self.left:
    #         if self.isJumping:
    #             game_display.blit(jumpLeft, (self.pos.x, self.pos.y))
    #         else:
    #             game_display.blit(walkLeft[self.walkCount//3], (self.pos.x, self.pos.y))
    #             self.walkCount += 1
    #     else:
    #         game_display.blit(stand_still, (self.pos.x, self.pos.y))
    #     self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    #     pygame.draw.rect(game_display, (255, 0, 0), self.rect, 2)

    # def collision_below(self, y, blocks):
    #     for block in blocks:
    #         if self.y > block.y and self.x in range(block.x, stop=block.x_range):
    #             self.y = block.y
    #         else:
    #             self.y = y
