import random

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.speed_x = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        self.speed_y = random.choice([-1, 1]) * random.uniform(0.5, 1.5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_horizontal(self):
        self.speed_x *= -1

    def bounce_vertical(self):
        self.speed_y *= -1

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        self.speed_y = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
