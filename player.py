import pygame
import settings as stg

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, game):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vec(self.x, self.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.game = game
        self.image = stg.stand_still
        self.rect = self.image.get_rect(bottomleft=(self.pos.x, self.pos.y))
        self.walkCount = 0
        self.left = False
        self.right = True
        self.isJumping = False

    def jump(self):
        self.rect.x += 1
        collision = pygame.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.x -= 1
        if collision:
            self.vel.y = -12
            self.isJumping = True

    def update(self):
        self.acc = vec(0, 0.34)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.pos.x > (self.rect.size[0]/2):
            self.acc.x = -stg.player_acc
            self.left = True
            self.right = False
        elif keys[pygame.K_RIGHT] and self.pos.x <= (self.game.map.width - 3*(self.rect.size[0]/2)):
            self.acc.x = stg.player_acc
            self.left = False
            self.right = True
        else:
            self.right = False
            self.left = False

        self.acc.x += self.vel.x * stg.player_friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.bottomleft = self.pos

    def draw(self, game_display):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.right:
            if self.isJumping:
                game_display.blit(
                    stg.jumpRight, (self.pos.x, self.pos.y - self.height))
            else:
                game_display.blit(
                    stg.walkRight[self.walkCount//3], (self.pos.x, self.pos.y - self.height))
                self.walkCount += 1
        elif self.left:
            if self.isJumping:
                game_display.blit(
                    stg.jumpLeft, (self.pos.x, self.pos.y - self.height))
            else:
                game_display.blit(
                    stg.walkLeft[self.walkCount//3], (self.pos.x, self.pos.y - self.height))
                self.walkCount += 1
        else:
            game_display.blit(
                stg.stand_still, (self.pos.x, self.pos.y - self.height))
        pygame.draw.rect(game_display, (255, 0, 0), self.rect, 2)

    # def collision_below(self, y, blocks):
    #     for block in blocks:
    #         if self.y > block.y and self.x in range(block.x, stop=block.x_range):
    #             self.y = block.y
    #         else:
    #             self.y = y
