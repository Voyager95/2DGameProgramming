from pico2d import *
import gfw
from gobj import *
import time


class textAlert:
    SIZE = 100

    def __init__(self, font, text, l, b, w, h, duration):
        self.startTime = time.time()
        self.font = font
        self.text = text
        self.l = l
        self.b = b
        self.w = w
        self.h = h
        self.duration = duration

    def draw(self):
        self.draw_centered_text(self.font, self.text,
                                self.l, self.b, self.w, self.h)

    def update(self):
        if time.time() > self.startTime + self.duration:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_text_extent(self, font, text):
        w, h = c_int(), c_int()
        TTF_SizeText(font.font, text.encode('utf-8'),
                     ctypes.byref(w), ctypes.byref(h))
        return w.value, h.value

    def draw_centered_text(self, font, text, l, b, w, h):
        tw, th = self.get_text_extent(font, text)
        tx = l + (w - tw) // 2
        ty = b + h // 2
        font.draw(tx, ty, text)
