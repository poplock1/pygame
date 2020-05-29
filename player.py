import pygame
import settings as stg

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


class player(object):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = stand_still
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vel = 12
        self.isJumping = False
        self.jumpCount = 11
        self.left = False
        self.right = False
        self.walkCount = 0

    def update(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] and self.x > (self.rect.size[0]/2):
            self.x -= self.vel
            self.right = False
            self.left = True
        elif self.keys[pygame.K_RIGHT] and self.x <= (stg.display_width - 3*(self.rect.size[0]/2)):
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if self.keys[pygame.K_SPACE]:
            self.isJumping = True

        if self.isJumping:
            neg = 1
            if self.jumpCount >= -11:
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJumping = False
                self.jumpCount = 11

    def draw(self, game_display):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.right:
            if self.isJumping:
                game_display.blit(jumpRight, (self.x, self.y))
            else:
                game_display.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        elif self.left:
            if self.isJumping:
                game_display.blit(jumpLeft, (self.x, self.y))
            else:
                game_display.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            game_display.blit(stand_still, (self.x, self.y))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        pygame.draw.rect(game_display, (255, 0, 0), self.rect, 2)

    # def collision_below(self, y, blocks):
    #     for block in blocks:
    #         if self.y > block.y and self.x in range(block.x, stop=block.x_range):
    #             self.y = block.y
    #         else:
    #             self.y = y
