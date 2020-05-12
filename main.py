import pygame
from player import player
# from pygame.locals import *

# class Car:

#     def __init__(self, image):
#         self.position = self.x_axis, self.y_axis = 100, 100
#         self.look = pygame.image.load('pic.png')
# class App:

#     def __init__(self):
#         self._running = True
#         self._display_surf = None
#         self.size = self.weight, self.height = 800, 600

#     def on_init(self):
#         pygame.init()
#         self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
#         self._running = True

#     def on_event(self, event):
#         if event.type == pygame.QUIT:
#             self._running = False

#     def on_loop(self):
#         pass

#     def on_render(self):
#         pass

#     def on_cleanup(self):as py
#         pygame.quit()

#     def on_excecute(self):
#         if self.on_init() == False:
#             self._running = False

#         while( self._running ):
#             for event in pygame.event.get():
#                 self.on_event(event)

#             gameDisplay.fill(white)
#             self.on_loop()
#             self.on_render()

#         self.on_cleanup()

# if __name__ == "__main__":
#     theApp = App()
#     theApp.on_excecute()

pygame.init()

display_width = 800
display_heigh = 700

gameDisplay = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption("Platform")

clock = pygame.time.Clock()


def draw():
    global walkCount
    gameDisplay.fill((0, 0, 0))
    player.draw(gameDisplay)
    pygame.display.update()


player = player(400, 600, 20, 20)
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
        if player.jumpCount >= -10:
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJumping = False
            player.jumpCount = 10

    draw()

pygame.quit()
