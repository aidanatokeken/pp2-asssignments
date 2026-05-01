import pygame, sys
from pygame.locals import *
import random

pygame.init()

# ================= НАСТРОЙКИ =================
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0  # счетчик монет

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Шрифт
font_small = pygame.font.SysFont("Verdana", 20)

# Экран
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# ================= КЛАСС ИГРОКА =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # создаем синий прямоугольник вместо картинки
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# ================= КЛАСС ВРАГА =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # красный прямоугольник
        self.image = pygame.Surface((40, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

# ================= КЛАСС МОНЕТ =================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # золотой квадрат
        self.image = pygame.Surface((20, 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(20, SCREEN_WIDTH-20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

# ================= СОЗДАНИЕ ОБЪЕКТОВ =================
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# ================= GAME LOOP =================
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    # ===== ОТОБРАЖЕНИЕ СЧЕТА =====
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)

    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # ===== ДВИЖЕНИЕ И ОТРИСОВКА =====
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # ===== СБОР МОНЕТ =====
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COINS_COLLECTED += 1
            coin.reset()

    # ===== СТОЛКНОВЕНИЕ С ВРАГОМ =====
    if pygame.sprite.spritecollideany(P1, enemies):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)