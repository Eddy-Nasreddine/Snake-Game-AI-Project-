import pygame
import random

background_colour = (255, 0, 0)
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Snake Game')
pygame.display.flip()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.update()

class Game:
    def __init__(self, screen):
        pass

class Snake:
    def __init__(self, length):
        self.length = 1
