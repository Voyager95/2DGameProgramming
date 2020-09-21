from pico2d import *
import random


class Boy:
    age = 10

    def __init__(self):  # __init__: 생성자 / self: 해당 인스턴스가 불려온 것
        self.x, self.y = random.randint(100, 700), random.randint(100, 500)
        self.img = load_image('./Resources/Images/run_animation.png')
        self.dx = random.random()
        self.fidx = random.randint(0, 7)

    def draw(self):
        self.img.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.dx * 5
        self.fidx = (self.fidx + 1) % 8


class Grass:
    def __init__(self):
        self.x, self.y = 400, 30
        self.img = load_image('./Resources/Images/grass.png')

    def draw(self):
        self.img.draw(self.x, self.y)
