from pico2d import *

open_canvas()

grass = load_image('./Resources/Images/grass.png')
character = load_image('./Resources/Images/run_animation.png')

x = 0
frame = 0
while(x < 800):
    clear_canvas()  # Game Rendering
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)

    x = x+2  # Game Logic
    frame = (frame + 1) % 8

    update_canvas()
    delay(.01)
    get_events()

close_canvas()
