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
pygame.display.set_caption("Racier")
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
clock = pygame.time.Clock()

def draw():
    global walkCount
    gameDisplay.fill((0,0,0))
    if walkCount + 1 >= 33:
        walkCount = 0
    if turn_right:
        if isJumping:
            gameDisplay.blit(jumpRight, (x, y))
        else:
            gameDisplay.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
    elif turn_left:
        if isJumping:
            gameDisplay.blit(jumpLeft, (x, y))
        else:
            gameDisplay.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1
    else:
        gameDisplay.blit(stand_still, (x,y))
    pygame.display.update()

x = 400
y = 550
vel = 8
walkCount = 0
isJumping = False
jumpCount = 10
run = True

while run:
    clock.tick(33)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if x > 20 and x <= 780:
        if keys[pygame.K_LEFT]:
            x -= vel
            turn_right = False
            turn_left = True
        elif keys[pygame.K_RIGHT]:
            x += vel
            turn_right = True
            turn_left = False
        else:
            turn_right = False
            turn_left = False
            walkCount = 0
    else:
        run = False

    if keys[pygame.K_SPACE]:
        isJumping = True
    
    if isJumping:
        neg = 1
        if jumpCount >= -10:
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJumping = False
            jumpCount = 10

    draw()
    

pygame.quit()