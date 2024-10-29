import pygame
import sys

pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 360
WHITE = (255, 255, 255)
BLUE = (0, 232, 155)               

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JustGame")

background_image = pygame.image.load("assets/background.jpg").convert()

player_image = pygame.Surface((50, 50))
player_image.fill(BLUE)
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

gravity = 1.5 
player_jump = False
player_jump_speed = -15 

platforms = [
    pygame.Rect(100, 300, 100, 10),
    pygame.Rect(250, 200, 100, 10),
    pygame.Rect(400, 250, 100, 10),
    pygame.Rect(550, 150, 100, 10)
]

def show_menu():
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render("JustGame", True, BLUE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        start_text = font.render("Press ENTER to start", True, (0, 0, 0))
        quit_text = font.render("Press ESC to quit", True, (0, 0, 0))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()a

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def show_options_menu():
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render("Options", True, BLUE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        resume_text = font.render("Press ENTER to resume", True, (0, 0, 0))
        quit_text = font.render("Press ESC to quit", True, (0, 0, 0))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main_game():
    global player_x, player_y, player_jump, player_jump_speed
    player_jump = False
    player_jump_speed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        if keys[pygame.K_SPACE] and not player_jump:
            player_jump = True
            player_jump_speed = -15

        if player_jump:
            player_y += player_jump_speed
            player_jump_speed += gravity
        else:
            player_y += gravity

        if player_y >= SCREEN_HEIGHT - player_image.get_height():
            player_y = SCREEN_HEIGHT - player_image.get_height()
            player_jump = False

        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        for platform in platforms:
            if player_rect.colliderect(platform) and player_jump_speed >= 0:
                player_y = platform.top - player_image.get_height()
                player_jump = False
                player_jump_speed = 0

        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        screen.blit(player_image, (player_x, player_y))

        for platform in platforms:
            pygame.draw.rect(screen, (0, 0, 0), platform)

        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            show_options_menu()

        pygame.time.Clock().tick(60)

show_menu()
main_game()
