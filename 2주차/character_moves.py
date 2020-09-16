from pico2d import *

open_canvas()

grass = load_image('./Resources/Images/grass.png')
character = load_image('./Resources/Images/character.png')

x = 0
while(x < 800):
    clear_canvas()  # Game Rendering
    grass.draw(400, 30)
    character.draw(x, 90)

    x = x+2  # Game Logic

    update_canvas()
    delay(.01)
    get_events()

close_canvas()
