import pygame
import random

def main():
    background_colour = (255, 0, 0)
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Snake Game')
    pygame.display.flip()
    running = True
    background_image = pygame.image.load('grid.png').convert()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.screen.blit(background_image,(0,0))
        a = pygame.Rect(500,500,50,50)
        a.center = (500,500)
        pygame.draw.rect(screen,(255,255,255),a)
        
        #rectangle = Rectangle(screen,50)
        #rectangle.draw_rectangle(50)
        pygame.display.update()
        pass


    
class Game:
    def __init__(self, screen):
        self.screen = screen


class Rectangle:
    def __init__(self,screen,length):
        self.length = length
    def draw_rectangle(length):
        pygame.draw.rect(screen,(255,255,255),length)


class Snake:
    def __init__(self, length,food):
        self.length = 2  
        self.food = 1
    def increase(length):
        #if snake eat food:
           #then increase length by 1
        pass
    def collision():
        #if snake hits out of bounds or snake hits itself:
            #game over
        pass

main()