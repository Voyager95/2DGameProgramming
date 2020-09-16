from pico2d import *


def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

grass = load_image('./Resources/Images/grass.png')
character = load_image('./Resources/Images/run_animation.png')

x = 0
frame = 0
running = True
while(x < 800 and running):
    clear_canvas()  # Game Rendering
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)

    x = x+2  # Game Logic
    frame = (frame + 1) % 8

    update_canvas()
    delay(.01)
    handle_events()

close_canvas()
