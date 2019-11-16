import pygame, sys
from pygame.locals import *
import pygame.gfxdraw
import game

pygame.init()

WIDTH = game.width
HEIGHT = game.height
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(game.white)

initial_world = game.Initial_world()
to_draw = game.draw(initial_world)
print(to_draw)

screen.blit(to_draw, (0, 0))
pygame.display.flip()

pygame.display.set_caption('My Game')

pygame.display.flip()

while True: # the main game loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
