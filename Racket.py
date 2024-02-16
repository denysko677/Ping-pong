class Racket:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def check_boundary(self, screen_height):
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
