import random
import time
from pico2d import *
import gfw
import gobj
import InputSystem
import os
import math
from button import Button
import record_state
import play_state

#--- Setting
targetScene = "record"

#--- Page
musicNumPerList = 4
maxPageNum = 0
musicFileNum = 0
musicList = []
presentPage = 0
musicButtonList = []

#--- Resource
font = None
bgm = None


def select(musicName):
    if targetScene == 'play':
        play_state.playMusicName = musicName
        gfw.push(play_state)
    else:
        record_state.recordMusicName = musicName
        gfw.push(record_state)


def set_music_count():
    global musicList, presentPage, maxPageNum, musicNumPerList

    musicList = os.listdir(gobj.RES_DIR + gobj.MUSIC_DIR)

    for i in musicList[:]:
        if -1 == i.find('.mp3'):
            musicList.remove(i)

    if targetScene != 'record':
        originList = os.listdir(gobj.RES_DIR + gobj.MUSIC_DIR)
        for i in musicList[:]:
            jfrFileName = i.replace('.mp3', '.jfr')
            found = False
            for o in originList:
                if o == jfrFileName:
                    found = True
            if found == False:
                musicList.remove[i]

    maxPageNum = math.ceil(len(musicList) / musicNumPerList)

    presentPage = 0
    pass


def set_page():
    global musicList, presentPage, musicNumPerList

    startIndex = presentPage * musicNumPerList
    endIndex = 0
    if startIndex + musicNumPerList - 1 > len(musicList):
        endIndex = len(musicList)
    else:
        endIndex = startIndex + musicNumPerList

    l, b, w, h = gobj.canvas_width/2 - 576/2, 520, 576, 116
    for i in range(startIndex, endIndex):
        musicName = musicList[i]
        b -= 116
        btn = Button(l, b, w, h, font,
                     musicList[i], lambda: select(musicName))
        btn.normalBg = ('Music', 'Normal')
        btn.hoverBg = ('Music', 'Normal')
        btn.pressedBg = ('Music', 'Pressed')
        btn.update_Img()
        gfw.world.add(gfw.layer.ui, btn)

    if endIndex - startIndex != musicNumPerList:
        for i in range(endIndex, startIndex + musicNumPerList):
            b -= 116
            btn = Button(l, b, w, h, font, '', lambda: None)
            btn.normalBg = ('Empty', 'Normal')
            btn.hoverBg = ('Empty', 'Normal')
            btn.pressedBg = ('Empty', 'Normal')
            btn.update_Img()
            gfw.world.add(gfw.layer.ui, btn)

    pass


def clear_page():
    for b in musicButtonList:
        gfw.world.remove(b)
    pass


def page_left():
    global maxPageNum, presentPage

    if presentPage - 1 >= 0:
        presentPage -= 1

    set_page()


def page_right():
    global maxPageNum, presentPage

    if presentPage + 1 <= maxPageNum:
        presentPage += 1

    set_page()


def enter():
    gfw.world.init(['bg', 'note', 'ui'])

    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Select_Bg.png', (get_canvas_width()//2, get_canvas_height()//2)))

    # --- Font
    global font
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 20)

    # --- BGM
    global bgm
    bgm = load_music(gobj.res('Bgm_Main.mp3'))
    bgm.repeat_play()

    # --- 음악 초기화
    set_music_count()

    # --- 버튼 생성

    # -- 페이지 이동 버튼 생성
    l, b, w, h = gobj.canvas_width/2 - 160*0.5 - \
        400, gobj.canvas_height/2 - 100, 154, 160
    btn = Button(l, b, w, h, font, '', lambda: page_left())
    btn.normalBg = ('Left', 'Normal')
    btn.hoverBg = ('Left', 'Normal')
    btn.pressedBg = ('Left', 'Normal')
    btn.update_Img()
    gfw.world.add(gfw.layer.ui, btn)

    l += 800
    btn = Button(l, b, w, h, font, '', lambda: page_right())
    btn.normalBg = ('Right', 'Normal')
    btn.hoverBg = ('Right', 'Normal')
    btn.pressedBg = ('Right', 'Normal')
    btn.update_Img()
    gfw.world.add(gfw.layer.ui, btn)

    set_page()
    pass


def update():
    gfw.world.update()
    pass


def draw():
    gfw.world.draw()
    pass


def handle_event(e):

    if e.type == SDL_QUIT:
        return gfw.quit()

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


def pause():
    pass


def exit():

    global bgm
    bgm.stop()

    pass


if __name__ == '__main__':
    gfw.run_main()
