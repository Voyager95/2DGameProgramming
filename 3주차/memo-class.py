from pico2d import *
from random import randint as rint
from random import random as rfloat

# 주제 클래스의 활용


class Boy:
    age = 10

    def __init__(self):  # __init__: 생성자 / self: 해당 인스턴스가 불려온 것
        self.x, self.y = rint(100, 700), rint(100, 500)
        self.img = load_image('./Resources/Images/run_animation.png')
        self.dx = rfloat()
        self.fidx = rint(0, 7)

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


def handle_events():
    global running
    global dir
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


open_canvas()

# 객체 생성

team = [Boy() for i in range(11)]
grass = Grass()

# 루프

running = True
while(running):
    clear_canvas()  # Game Rendering

    grass.draw()

    update_canvas()

    handle_events()  # Game Logic

    delay(.01)


close_canvas()
