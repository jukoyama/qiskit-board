import pygame, sys
from pygame.locals import *
import pygame.gfxdraw
import game

pygame.init()

BIG_BANG = game.big_bang

WIDTH = BIG_BANG.width
HEIGHT = BIG_BANG.height
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(game.white)

INITIAL_WORLD = game.initial_world
TO_DRAW = BIG_BANG.to_draw
print(TO_DRAW)

SCREEN.blit(TO_DRAW, (0, 0))
pygame.display.flip()

pygame.display.set_caption('My Game')

pygame.display.flip()

while True: # the main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
