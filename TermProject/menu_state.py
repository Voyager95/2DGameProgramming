from pico2d import *
import gfw
import gobj
from button import Button
import pair_state
import record_state
import select_state


def start(theme):
    pair_state.theme = theme
    gfw.push(pair_state)


def push_play_select():
    select_state.targetScene = 'play'
    gfw.push(select_state)


def push_record_select():
    select_state.targetScene = 'record'
    gfw.push(select_state)


def build_world():
    gfw.world.init(['bg', 'ui'])

    center = (gobj.canvas_width//2, gobj.canvas_height//2)
    bg = gobj.ImageObject('Title_Bg.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    # Button(l, b, w, h, font, text, callback, btnClass=None):
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 40)

    l, b, w, h = gobj.canvas_width/2 - 270/2, 120, 270, 140
    btn = Button(l, b, w, h, font, '', lambda: push_play_select())
    btn.normalBg = ('Play', 'Normal')
    btn.hoverBg = ('Play', 'Hover')
    btn.pressedBg = ('Play', 'Pressed')
    btn.update_Img()
    gfw.world.add(gfw.layer.ui, btn)

    b -= 100
    btn = Button(l, b, w, h, font, "", lambda: push_record_select())
    btn.normalBg = ('Record', 'Normal')
    btn.hoverBg = ('Record', 'Hover')
    btn.pressedBg = ('Record', 'Pressed')
    btn.update_Img()
    gfw.world.add(gfw.layer.ui, btn)

    global bgm
    bgm = load_music(gobj.res('Bgm_Main.mp3'))
    bgm.repeat_play()


def enter():
    build_world()


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()


def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    # print('ms.he()', e.type, e)
    if handle_mouse(e):
        return


capture = None


def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False


def exit():
    print("menu_state exits")

    global bgm
    bgm.stop()
    pass


def pause():
    pass


def resume():
    build_world()


if __name__ == '__main__':
    gfw.run_main()
