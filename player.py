import pygame

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

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJumping = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, gameDisplay):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.right:
            if self.isJumping:
                gameDisplay.blit(jumpRight, (self.x, self.y))
            else:
                gameDisplay.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        elif self.left:
            if self.isJumping:
                gameDisplay.blit(jumpLeft, (self.x, self.y))
            else:
                gameDisplay.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            gameDisplay.blit(stand_still, (self.x, self.y))
