import pygame
import sys
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mygame"]
players_collection = db["players"]

pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 360
WHITE = (255, 255, 255)
BLUE = (0, 232, 155)               

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JustGame")

font = pygame.font.Font(None, 36)

def save_player(username, password):
    players_collection.insert_one({"username": username, "password": password})

def get_player(username, password):
    return players_collection.find_one({"username": username, "password": password})

def render_text(text, position, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def get_text_input(prompt):
    user_text = ""
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        screen.fill(WHITE)
        render_text(prompt, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3))
        render_text(user_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3 + 50), BLUE)
        pygame.display.flip()
    
    return user_text

def show_login_screen():
    while True:
        screen.fill(WHITE)
        render_text("JustGame - Login", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 4), BLUE)
        render_text("1. Register", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        render_text("2. Login", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 40))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    username = get_text_input("Enter new username:")
                    password = get_text_input("Enter new password:")
                    if players_collection.find_one({"username": username}):
                        render_text("Username already exists!", (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 80), (255, 0, 0))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                    else:
                        save_player(username, password)
                        render_text("Account created successfully!", (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 80), (0, 255, 0))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        return username
                elif event.key == pygame.K_2:
                    username = get_text_input("Enter username:")
                    password = get_text_input("Enter password:")
                    if get_player(username, password):
                        render_text("Login successful!", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 80), (0, 255, 0))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        return username
                    else:
                        render_text("Incorrect username or password.", (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 80), (255, 0, 0))
                        pygame.display.flip()
                        pygame.time.wait(2000)

def show_menu():
    while True:
        screen.fill(WHITE)
        title_text = font.render("JustGame", True, BLUE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))

        start_text = font.render("Press ENTER to start", True, (0, 0, 0))
        quit_text = font.render("Press ESC to quit", True, (0, 0, 0))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
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

def main_game(username):
    print(f"Bienvenue dans le jeu, {username}!")

username = show_login_screen()
if username:
    show_menu()
    main_game(username)
