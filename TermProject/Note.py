from pico2d import *
import gfw
from gobj import *


class note:
    SIZE = 100

    def __init__(self, x, y, speed, noteType):
        self.x, self.y = x, y
        if noteType == '1' or noteType == '2' or noteType == '3' or noteType == '4':
            self.image = gfw.image.load(
                RES_DIR + '/Note_%d.png' % int(noteType))
        elif noteType == 'down':
            self.image = gfw.image.load(RES_DIR + '/Note_Down.png')
        elif noteType == 'up':
            self.image = gfw.image.load(RES_DIR + '/Note_Up.png')
        self.dy = speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        #self.time += gfw.delta_time
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height():
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        half = note.SIZE // 2 - 5
        return self.x - half, self.y - half, self.x + half, self.y + half
