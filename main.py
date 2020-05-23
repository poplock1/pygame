import pygame
from player import player
from blocks import block

display_width = 800
display_heigh = 700
FPS = 33

block_img = pygame.image.load("grass.png")

pygame.init()

game_display = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption("Platform")
clock = pygame.time.Clock()


def draw():
    game_display.fill((150, 150, 140))
    for element in blocks:
        element.draw(game_display)
    player.draw(game_display)
    pygame.display.flip()


player = player(400, 600)
blocks = [block(200, 500, block_img), block(300, 500, block_img)]
run = True

while run:
    # Process input (events)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
    # Update
    if keys[pygame.K_LEFT] and player.x > (player.rect.size[0]/2):
        player.x -= player.vel
        player.right = False
        player.left = True
    elif keys[pygame.K_RIGHT] and player.x <= (display_width - 3*(player.rect.size[0]/2)):
        player.x += player.vel
        player.right = True
        player.left = False
    else:
        player.right = False
        player.left = False
        player.walkCount = 0

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

    # Draw
    draw()

pygame.quit()
