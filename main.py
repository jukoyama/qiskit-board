import pygame, sys
from pygame.locals import *
import pygame.gfxdraw
import game

pygame.init()

BIG_BANG = game.big_bang

WIDTH = BIG_BANG.width
HEIGHT = BIG_BANG.height

#set up the window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(game.white)

INITIAL_WORLD = game.initial_world
TO_DRAW = BIG_BANG.to_draw

SCREEN.blit(TO_DRAW, (0, 0))
pygame.display.flip()

pygame.display.set_caption('My Game')

pygame.display.flip()

is_running = True
while is_running: # the main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                print("H gate!")
                game.on_key("h", game.initial_world, SCREEN)
            elif event.key == pygame.K_x:
                print("X gate!")
                game.on_key("x", game.initial_world, SCREEN)
                # SCREEN.blit(IMAGE, (0, 0))
            elif event.key == pygame.K_c:
                print("C gate!")
                game.on_key("c", game.initial_world, SCREEN)

    if BIG_BANG.stop_when == True:
        is_running = False

    pygame.display.update()
