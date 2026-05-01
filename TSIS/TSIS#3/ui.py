import pygame
from racer import Game

pygame.init()

class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Racer Menu")
        self.font = pygame.font.SysFont(None, 40)

    def run(self):
        username = ""
        active = True

        while True:
            self.screen.fill((30, 30, 30))

            # текст
            text = self.font.render("Enter your name:", True, (255, 255, 255))
            name_surface = self.font.render(username, True, (0, 255, 0))

            self.screen.blit(text, (80, 200))
            self.screen.blit(name_surface, (80, 260))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # 👉 запускаем игру сразу после Enter
                        game = Game()
                        game.run(username if username else "Player")
                        return

                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]

                    else:
                        username += event.unicode