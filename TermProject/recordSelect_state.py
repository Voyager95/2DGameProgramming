import random
import time
from pico2d import *
import gfw
import gobj
import InputSystem


def enter():
    gfw.world.init(['bg', 'note', 'ui'])
    pass


def update():
    gfw.world.update()
    pass


def draw():
    gfw.world.draw()
    pass


def handle_event(e):
    pass


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
