import pygame
from player import player
from blocks import block

pygame.init()

display_width = 800
display_heigh = 700

gameDisplay = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption("Platform")

clock = pygame.time.Clock()


def draw():
    gameDisplay.fill((0, 0, 0))
    block1.draw(gameDisplay)
    block2.draw(gameDisplay)
    player.draw(gameDisplay)
    pygame.display.update()


player = player(400, 600, 20, 20)
block1 = block(200,500)
block2 = block(300,500)
run = True

while run:
    clock.tick(33)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if player.x > 20 and player.x <= 780:
        if keys[pygame.K_LEFT]:
            player.x -= player.vel
            player.right = False
            player.left = True
        elif keys[pygame.K_RIGHT]:
            player.x += player.vel
            player.right = True
            player.left = False
        else:
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
        run = False

    if keys[pygame.K_SPACE]:
        player.isJumping = True

    if player.isJumping:
        neg = 1
        if player.jumpCount >= -11:
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJumping = False
            player.jumpCount = 11

    draw()

pygame.quit()
