import pygame
import random
import time
def main():
    background_colour = (255, 0, 0)
    screen = pygame.display.set_mode((995, 995))
    pygame.display.set_caption('')
    pygame.display.flip()
    running = True
    background_image = pygame.image.load('995 grid.png').convert()
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    snakey = Snake(screen)
    x_pos = 500
    y_pos = 500
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image,(0,0))
        #snakey.Food(x,y)


        snakey.draw_snake(x_pos, y_pos)
        userinput = pygame.key.get_pressed()
        print(x_pos, ":",y_pos)
        if userinput[pygame.K_w]:
            #while True:
            y_pos -= 5
                # if (userinput[pygame.K_a] or userinput[pygame.K_d]):
                #     break\
            print("w")
        elif userinput[pygame.K_s]:
            #while True:
            y_pos += 5
                # if (userinput[pygame.K_d] or userinput[pygame.K_a]):
                #     break
            print("s")
        elif userinput[pygame.K_a]:
            #while True:
            x_pos -= 5
                # if (userinput[pygame.K_w] or userinput[pygame.K_s]):
                #     break
            print("a")
        elif userinput[pygame.K_d]:
            # while True:
            x_pos += 5
            print("d")
                # if (userinput[pygame.K_w] or userinput[pygame.K_s]):
                #     break

        pygame.time.Clock().tick(60)
        pygame.display.flip()
        pass


class Snake:
    def __init__(self, screen):
        self.screen = screen
    def draw_snake(self, x_pos, y_pos):
        a = pygame.Rect(x_pos, y_pos, 50, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), a)
    def increase(length):
        #if snake eat food:
           #then increase length by 1
        pass
    def collision():
        #if snake hits out of bounds or snake hits itself:
            #game over
        pass
    def Food(x_pos ,y_pos):

        food = pygame.Rect(x_pos, y_pos, 50, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), food)


main()

