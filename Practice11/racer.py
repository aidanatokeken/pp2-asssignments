import pygame, sys
from pygame.locals import *
import random

pygame.init()

# ================= НАСТРОЙКИ =================
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

BASE_SPEED = 5
SPEED = BASE_SPEED

SCORE = 0
COINS_COLLECTED = 0

# через сколько монет увеличивается скорость
LEVEL_UP_COINS = 5  

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)

font_small = pygame.font.SysFont("Verdana", 20)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# ================= PLAYER =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# ================= ENEMY =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        # случайное положение сверху
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)

        # если враг прошел экран → увеличиваем SCORE
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset()

# ================= COIN =================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.set_random_type()

    def set_random_type(self):
        # выбираем случайный "вес" монеты
        self.value = random.choice([1, 3, 5])

        # меняем цвет и размер в зависимости от ценности
        if self.value == 1:
            self.image = pygame.Surface((15, 15))
            self.image.fill(BRONZE)
        elif self.value == 3:
            self.image = pygame.Surface((20, 20))
            self.image.fill(SILVER)
        else:
            self.image = pygame.Surface((25, 25))
            self.image.fill(GOLD)

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        # новое случайное положение
        self.rect.center = (random.randint(20, SCREEN_WIDTH-20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            # если не собрали — генерируем новую монету
            self.set_random_type()

# ================= СОЗДАНИЕ =================
P1 = Player()
E1 = Enemy()

coins = pygame.sprite.Group()
for _ in range(2):  # сразу несколько монет
    coins.add(Coin())

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# ================= GAME LOOP =================
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((200, 200, 200))

    # ===== ТЕКСТ =====
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    speed_text = font_small.render(f"Speed: {SPEED}", True, BLACK)

    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (250, 10))
    DISPLAYSURF.blit(speed_text, (10, 40))

    # ===== ДВИЖЕНИЕ =====
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # ===== СБОР МОНЕТ =====
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COINS_COLLECTED += coin.value  # добавляем вес монеты
            coin.set_random_type()

    # ===== УВЕЛИЧЕНИЕ СКОРОСТИ =====
    if COINS_COLLECTED // LEVEL_UP_COINS > (SPEED - BASE_SPEED):
        SPEED += 1  # увеличиваем скорость

    # ===== СТОЛКНОВЕНИЕ =====
    if pygame.sprite.spritecollideany(P1, enemies):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)