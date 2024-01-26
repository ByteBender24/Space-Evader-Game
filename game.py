import pygame
import random
import time

# source C:/Users/HARI/.virtualenvs/Space_Evader-eCkaBzOt/Scripts/activate

pygame.font.init()  # initialize font module for rendering elapsed time (font object)

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Evader")

BG = pygame.transform.scale(pygame.image.load(
    r"./assets/bg.jpeg"), (WIDTH, HEIGHT))

# normal => BG = pygame.image.load(path, (coord as tuple)) ==================================== ref docs for different scaling for background image

PLAYER_HEIGHT = 60
PLAYER_WIDTH = 40

PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time):

    #window
    WIN.blit(BG, (0, 0))
    
    #elapsed_time
    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "white")   #1 ---> anti-aliasing
    WIN.blit(time_text, (10,10))

    #player-character
    pygame.draw.rect(WIN, (255, 0, 0), player)  # also can use "red"
    pygame.display.update()


def main():

    run = True

    # to center the player on x axis -> WIDTH//2 - PLAYER_WIDTH , to make the player on base -> HEIGHT - PLAYER_HEIGHT
    player = pygame.Rect(WIDTH//2 - PLAYER_WIDTH, HEIGHT -
                         PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    # for elapsed time
    start_time = time.time()
    elapsed_time = 0

    while run:

        clock.tick(60)  # framerate = 60

        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        # to check the boundaries by adding guard conditionals
        if keys[pygame.K_LEFT] and (player.x - PLAYER_VEL >= 0):
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and (player.x + PLAYER_VEL + player.width <= WIDTH):
            player.x += PLAYER_VEL

        if keys[pygame.K_UP] and (player.y + PLAYER_VEL >= 0):
            player.y -= PLAYER_VEL

        if keys[pygame.K_DOWN] and (player.y + PLAYER_VEL + player.height <= HEIGHT):
            player.y += PLAYER_VEL

        draw(player, elapsed_time)

    pygame.quit()


if __name__ == "__main__":
    main()
