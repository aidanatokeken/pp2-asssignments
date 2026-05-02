import pygame
import sys
import json

from game import SnakeGame
from db import *
from config import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

init_db()

# ---------------- SETTINGS ----------------
def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {"snake_color": [0,255,0], "grid": True, "sound": True}

settings = load_settings()

# ---------------- USER ----------------
def get_username():
    name = ""

    while True:
        screen.fill(BLACK)
        txt = font.render("Username: " + name, True, WHITE)
        screen.blit(txt, (150, 300))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return name
                elif e.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += e.unicode

# ---------------- LEADERBOARD ----------------
def show_leaderboard():
    data = leaderboard()

    run = True
    while run:
        screen.fill(BLACK)

        y = 50
        title = font.render("LEADERBOARD", True, WHITE)
        screen.blit(title, (200, 20))

        for i, r in enumerate(data):
            line = font.render(f"{i+1}. {r[0]} - {r[1]} pts", True, WHITE)
            screen.blit(line, (50, y))
            y += 40

        hint = font.render("ESC to back", True, RED)
        screen.blit(hint, (200, 500))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                run = False

# ---------------- GAME ----------------
def play(player_id):
    game = SnakeGame(player_id)

    while not game.game_over:
        clock.tick(game.speed)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    game.dx, game.dy = -CELL, 0
                if e.key == pygame.K_RIGHT:
                    game.dx, game.dy = CELL, 0
                if e.key == pygame.K_UP:
                    game.dx, game.dy = 0, -CELL
                if e.key == pygame.K_DOWN:
                    game.dx, game.dy = 0, CELL

        game.move()
        game.update_power()

        screen.fill(BLACK)

        for s in game.snake:
            pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

        pygame.draw.rect(screen, BLUE, (*game.food, CELL, CELL))
        pygame.draw.rect(screen, DARK_RED, (*game.poison, CELL, CELL))
        pygame.draw.rect(screen, YELLOW, (*game.power, CELL, CELL))

        for o in game.obstacles:
            pygame.draw.rect(screen, WHITE, (*o, CELL, CELL))

        score = font.render(f"Score: {game.score} Level: {game.level}", True, WHITE)
        screen.blit(score, (10, 10))

        pygame.display.flip()

    game.save()

# ---------------- MAIN MENU ----------------
def main():
    username = get_username()
    player_id = get_or_create_player(username)

    while True:
        screen.fill(BLACK)

        title = font.render("SNAKE GAME", True, WHITE)
        screen.blit(title, (200, 200))

        play_txt = font.render("SPACE - Play", True, GREEN)
        screen.blit(play_txt, (200, 300))

        lb_txt = font.render("L - Leaderboard", True, WHITE)
        screen.blit(lb_txt, (200, 350))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    play(player_id)
                if e.key == pygame.K_l:
                    show_leaderboard()

main()