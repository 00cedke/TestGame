import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fortnite-like Game")

player_image = pygame.Surface((50, 50))
player_image.fill(BLUE)

player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

gravity = 0.5
player_jump = False
player_jump_speed = -10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_SPACE] and not player_jump:
        player_jump = True
        player_jump_speed = -10

    if keys[pygame.K_z]:
        player_y -= player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    if player_y < SCREEN_HEIGHT - player_image.get_height():
        player_y += gravity

    if player_jump:
        player_y += player_jump_speed
        player_jump_speed += gravity
        if player_y >= SCREEN_HEIGHT - player_image.get_height():
            player_jump = False

    screen.fill(WHITE)
    screen.blit(player_image, (player_x, player_y))
    pygame.display.flip()

    pygame.time.Clock().tick(60)
