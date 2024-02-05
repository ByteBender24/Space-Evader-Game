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

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3


def draw(player, elapsed_time, stars):

    # window
    WIN.blit(BG, (0, 0))

    # elapsed_time
    # 1 ---> anti-aliasing
    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    # player-character
    pygame.draw.rect(WIN, (255, 0, 0), player)  # also can use "red"
    pygame.display.update()


def add_stars(stars, star_delay_high_time, star_low_time):
    if star_delay_high_time > star_low_time:
        num_stars_to_add = 3
        new_stars = generate_stars(num_stars_to_add)
        stars.extend(new_stars)

        star_low_time = max(200, star_low_time - 50)
        star_delay_high_time = 0

    return star_low_time, star_delay_high_time


def generate_stars(num_stars):
    return [create_star() for _ in range(num_stars)]


def create_star():
    star_x = random.randint(0, WIDTH - STAR_WIDTH)
    return pygame.Rect(star_x, 0-STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)  # 0-Star_Height for making it come from above screen


def check_collisions(player, stars):
    for star in stars[:]:
        star.y += STAR_VEL
        if star.y > HEIGHT:
            stars.remove(star)
        elif star.y + star.height >= player.y and star.colliderect(player):
            stars.remove(star)
            return True  # Player hit

    return False


def display_game_over():
    lost_text = FONT.render("You Lost!", 1, "white")
    WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width() /
             2, HEIGHT/2 - lost_text.get_height()/2))
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

    star_low_time = 2000
    star_delay_high_time = 0
    stars = []
    hit = False

    while run:

        star_delay_high_time += clock.tick(60)  # framerate = 60

        star_low_time, star_delay_high_time = add_stars(
            stars, star_delay_high_time, star_low_time)

        if check_collisions(player, stars):
            display_game_over()
            pygame.time.delay(4000)
            break

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

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
