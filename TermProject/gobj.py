import random
from pico2d import *
import gfw
import os

RES_DIR = './res/'
MUSIC_DIR = 'PlayMusic/'
# 전역
DRAW_CLIP = 0
DRAW_CENTER = 1

canvas_width = 1366
canvas_height = 768


def res(file):
    return RES_DIR + file


def resMusic(file):
    return RES_DIR + MUSIC_DIR + file


def resl(files):
    return [RES_DIR + f for f in files]


def rand(val):
    return val * random.uniform(0.9, 1.1)


def point_add(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return x1+x2, y1+y2


def move_obj(obj):
    obj.pos = point_add(obj.pos, obj.delta)


def collides_box(a, b):
    (la, ba, ra, ta) = a.get_bb()
    (lb, bb, rb, tb) = b.get_bb()

    if la > rb:
        return False
    if ra < lb:
        return False
    if ba > tb:
        return False
    if ta < bb:
        return False

    return True


def distance_sq(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x1-x2)**2 + (y1-y2)**2


def distance(point1, point2):
    math.sqrt(distance_sq(point1, point2))


def draw_collision_box():
    for obj in gfw.world.all_objects():
        if hasattr(obj, 'get_bb'):
            draw_rectangle(*obj.get_bb())


def mouse_xy(event):
    return event.x, get_canvas_height() - event.y - 1


def pt_in_rect(point, rect):
    (x, y) = point
    (l, b, r, t) = rect

    if x < l:
        return False
    if x > r:
        return False
    if y < b:
        return False
    if y > t:
        return False

    return True


class ImageObject:
    def __init__(self, imageName, pos):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.pos = pos

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        pass

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict

    def __setstate__(self, dict):
        self.__dict__.update(dict)
        self.image = gfw.image.load(res(self.imageName))

    def __del__(self):
        print('Del Img:', self)


class AnimObject:
    def __init__(self, imageName, pos, fps, fcount=0):
        self.time = get_time()
        self.image = gfw.image.load(RES_DIR + '/' + imageName)
        self.pos = pos
        self.fps = fps
        if fcount == 0:
            fcount = self.image.w // self.image.h
        self.width = self.image.w // fcount
        self.height = self.image.h
        self.fcount = fcount

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        sx = self.width * fidx
        self.image.clip_draw(sx, 0, self.width, self.height, *self.pos)

    def update(self):
        pass

    def __del__(self):
        print('Del Anim:', self)


if __name__ == "__main__":
    print("This file is not supposed to be executed directly.")
