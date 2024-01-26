import pygame
import random
import time

# source C:/Users/HARI/.virtualenvs/Space_Evader-eCkaBzOt/Scripts/activate

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Evader")

BG = pygame.transform.scale(pygame.image.load(r"./assets/bg.jpeg"), (WIDTH, HEIGHT))
#normal => BG = pygame.image.load(path, (coord as tuple))
#ref docs for different scaling for background image

def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()


def main():

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()


if __name__ == "__main__":
    main()
