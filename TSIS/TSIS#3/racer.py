import pygame, random, time
from persistence import load_settings, save_score

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Game:
    def __init__(self):
        self.settings = load_settings()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.speed = 5
        self.coins = 0
        self.distance = 0

        self.active_powerup = None
        self.powerup_timer = 0

        self.player = pygame.Rect(180, 500, 40, 60)
        self.obstacles = []
        self.powerups = []

    def spawn_obstacle(self):
        # SAFE SPAWN — не на игроке
        while True:
            x = random.randint(0, 360)
            rect = pygame.Rect(x, 0, 40, 60)
            if not rect.colliderect(self.player):
                self.obstacles.append(rect)
                break

    def spawn_powerup(self):
        types = ["nitro", "shield", "repair"]
        t = random.choice(types)

        rect = pygame.Rect(random.randint(0, 360), 0, 30, 30)
        self.powerups.append({"type": t, "rect": rect, "time": time.time()})

    def apply_powerup(self, p):
        # только один активен
        self.active_powerup = p["type"]

        if p["type"] == "nitro":
            self.speed += 3
            self.powerup_timer = time.time() + 4

        elif p["type"] == "shield":
            self.powerup_timer = None

        elif p["type"] == "repair":
            # моментальный эффект
            self.obstacles.clear()

    def update_powerup(self):
        if self.active_powerup == "nitro":
            if time.time() > self.powerup_timer:
                self.speed -= 3
                self.active_powerup = None

    def run(self, username):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.x -= 5
            if keys[pygame.K_RIGHT]:
                self.player.x += 5

            # === СПАВН ===
            if random.random() < 0.02:
                self.spawn_obstacle()

            if random.random() < 0.01:
                self.spawn_powerup()

            # === ДВИЖЕНИЕ ===
            for o in self.obstacles:
                o.y += self.speed

                if o.colliderect(self.player):
                    if self.active_powerup == "shield":
                        self.active_powerup = None
                        self.obstacles.remove(o)
                    else:
                        save_score(username, self.coins, self.distance)
                        running = False

            # === POWERUPS ===
            for p in self.powerups:
                p["rect"].y += self.speed

                # исчезают если не собрали
                if time.time() - p["time"] > 5:
                    self.powerups.remove(p)

                if p["rect"].colliderect(self.player):
                    self.apply_powerup(p)
                    self.powerups.remove(p)

            self.update_powerup()

            # === СЛОЖНОСТЬ ===
            self.distance += self.speed
            if self.distance % 500 == 0:
                self.speed += 1

            # === ОТРИСОВКА ===
            self.screen.fill((200, 200, 200))
            pygame.draw.rect(self.screen, (0,0,255), self.player)

            for o in self.obstacles:
                pygame.draw.rect(self.screen, (255,0,0), o)

            for p in self.powerups:
                color = (255,255,0)
                pygame.draw.rect(self.screen, color, p["rect"])

            pygame.display.update()
            self.clock.tick(60)