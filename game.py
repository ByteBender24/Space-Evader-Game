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

    player = pygame.Rect(WIDTH//2 - PLAYER_WIDTH, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)  # to center the player on x axis -> WIDTH//2 - PLAYER_WIDTH , to make the player on base -> HEIGHT - PLAYER_HEIGHT
    
    clock = pygame.time.Clock()

    while run:

        clock.tick(60) #framerate = 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and (player.x - PLAYER_VEL >= 0) : # to check the boundaries by adding guard conditionals
            player.x -= PLAYER_VEL

        # to check the boundaries by adding guard conditionals
        if keys[pygame.K_RIGHT] and (player.x + PLAYER_VEL + player.width <= WIDTH):
            player.x += PLAYER_VEL

        if keys[pygame.K_UP] and (player.y + PLAYER_VEL >= 0):
            print(player.y + player.height + PLAYER_VEL)
            player.y -= PLAYER_VEL

        if keys[pygame.K_DOWN] and (player.y + PLAYER_VEL + player.height <= HEIGHT):
            player.y += PLAYER_VEL
        draw(player)

        
    pygame.quit()


if __name__ == "__main__":
    main()
