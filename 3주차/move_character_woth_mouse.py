from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            # 윈도우 좌표계와 Pico2D의 좌표계의 Y가 반대이기 때문이다.
            x, y = event.x, KPU_HEIGHT - 1 - event.y


open_canvas(KPU_WIDTH, KPU_HEIGHT)

grass = load_image('./Resources/Images/grass.png')
character = load_image('./Resources/Images/run_animation.png')

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
running = True
hide_cursor()

while running:
    clear_canvas()  # Game Rendering
    grass.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(.01)


close_canvas()
