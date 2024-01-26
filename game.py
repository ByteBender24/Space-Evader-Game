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

PLAYER_HEIGHT = 60
PLAYER_WIDTH = 40

PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, (255, 0 ,0) , player) #also can use "red"
    pygame.display.update()


def main():

    run = True

    player = pygame.Rect(WIDTH//2 - PLAYER_WIDTH, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    
    # to center the player on x axis -> WIDTH//2 - PLAYER_WIDTH
    # to make the player on base -> HEIGHT - PLAYER_HEIGHT
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP]:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN]:
                    player.y += PLAYER_VEL
        draw(player)

        
    pygame.quit()


if __name__ == "__main__":
    main()
