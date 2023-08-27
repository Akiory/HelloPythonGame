import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 240))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, BLUE)
screen.blit(img, (20, 20))
pygame.display.update()