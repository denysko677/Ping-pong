import pygame
import sys

# Клас, що представляє базову гру
class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.is_running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        self.quit()

    def quit(self):
        pygame.quit()
        sys.exit()


# Клас, що представляє гру "Ping Pong"
class Pong(Game):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg_color = (0, 0, 0)
        self.ball_color = (255, 255, 255)
        self.ball_radius = 10
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_speed_x = 5
        self.ball_speed_y = 5

    def handle_events(self):
        super().handle_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Рухаємо щиток вгору
            pass
        if keys[pygame.K_DOWN]:
            # Рухаємо щиток вниз
            pass

    def update(self):
        # Оновлення руху м'яча
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        # Перевірка колізій зі стінами
        if self.ball_x + self.ball_radius >= self.width or self.ball_x - self.ball_radius <= 0:
            self.ball_speed_x *= -1
        if self.ball_y + self.ball_radius >= self.height or self.ball_y - self.ball_radius <= 0:
            self.ball_speed_y *= -1

    def draw(self):
        self.screen.fill(self.bg_color)
        pygame.draw.circle(self.screen, self.ball_color, (self.ball_x, self.ball_y), self.ball_radius)


if __name__ == "__main__":
    pygame.init()
    pong_game = Pong(800, 600, "Ping Pong")
    pong_game.run()
    