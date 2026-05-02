import pygame
import random
from config import *
from db import save_game


class SnakeGame:
    def __init__(self, player_id):
        self.player_id = player_id

        self.snake = [(100, 100)]
        self.dx = CELL
        self.dy = 0

        self.food = self.spawn()
        self.poison = self.spawn()
        self.power = self.spawn_power()

        self.power_type = None
        self.power_time = 0

        self.score = 0
        self.level = 1
        self.speed = FPS

        self.obstacles = []

        self.game_over = False

    # ---------------- SPAWN ----------------
    def spawn(self):
        return (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))

    def spawn_power(self):
        return self.spawn()

    # ---------------- OBSTACLES ----------------
    def generate_obstacles(self):
        self.obstacles = []

        if self.level < 3:
            return

        for _ in range(self.level * 4):
            self.obstacles.append(self.spawn())

    # ---------------- POWER ----------------
    def apply_power(self, p):
        now = pygame.time.get_ticks()

        if p == "speed":
            self.speed = FPS * 2
            self.power_time = now + 5000

        elif p == "slow":
            self.speed = max(5, FPS // 2)
            self.power_time = now + 5000

        elif p == "shield":
            self.power_type = "shield"

    def update_power(self):
        if self.power_time and pygame.time.get_ticks() > self.power_time:
            self.speed = FPS
            self.power_time = 0

    # ---------------- MOVE ----------------
    def move(self):
        head = self.snake[0]
        new = (head[0] + self.dx, head[1] + self.dy)

        # wall
        if new[0] < 0 or new[1] < 0 or new[0] >= WIDTH or new[1] >= HEIGHT:
            if self.power_type == "shield":
                self.power_type = None
            else:
                self.game_over = True
                return

        # self
        if new in self.snake:
            if self.power_type == "shield":
                self.power_type = None
            else:
                self.game_over = True
                return

        # obstacle
        if new in self.obstacles:
            self.game_over = True
            return

        self.snake.insert(0, new)

        # food
        if new == self.food:
            self.score += 1
            self.food = self.spawn()

            if self.score % 3 == 0:
                self.level += 1
                self.generate_obstacles()

        else:
            self.snake.pop()

        # poison
        if new == self.poison:
            self.snake.pop()
            self.snake.pop()
            self.poison = self.spawn()

            if len(self.snake) <= 1:
                self.game_over = True

        # power
        if new == self.power:
            self.apply_power(random.choice(["speed", "slow", "shield"]))
            self.power = self.spawn_power()

    # ---------------- SAVE ----------------
    def save(self):
        save_game(self.player_id, self.score, self.level)