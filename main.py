import pygame
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
    
#     def on_cleanup(self):
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
display_heigh = 600

gameDisplay = pygame.display.set_mode((display_width, display_heigh))
pygame.display.set_caption("Racier")
clock = pygame.time.Clock()

carImage = pygame.image.load('pic.png')

def car(x, y):
    gameDisplay.blit(carImage, (x,y))

x = 400
y = 50
vel = 5

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    gameDisplay.fill((255,255,255))
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()