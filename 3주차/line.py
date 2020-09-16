from turtle import *
import pico2d


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2-y1)/(x2-x1)
    b = y1 - x1 * a
    for x in range(x1, x2 + 1, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)


prepare_turtle_canvas()
draw_line_basic((-100, -100), (300, 150))
done()
