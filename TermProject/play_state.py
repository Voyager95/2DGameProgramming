import random
import time
from pico2d import *
import gfw
import gobj
import InputSystem
from note import note
from mutagen.mp3 import MP3
import json
import os
from textAlert import textAlert

# --- Setting
inputType = "stroke"
playMusicName = "ACDC - You Shook Me All Night Long.mp3"
music = None

# --- MusicTime
startTime = 0
endTime = 0

# --- Note
leftNoteCheckPos = 0
rightNoteCheckPos = 0

# --- Input
strokeInput = None
downInput = None
inputList = []

# --- SpecialKey
key_ctrl, key_s = False, False

# --- Resource
font = None


def inputTime():
    global startTime
    return time.time() - startTime


def onOneDownInput():
    pass


def onTwoDownInput():
    pass


def onThreeDownInput():
    pass


def onFourDownInput():
    pass


def onUpStrokeInput():
    pass


def onDownStokeInput():
    pass


def enter():
    gfw.world.init(['bg', 'note', 'ui'])

    # --- Resource
    global font
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 40)

    # --- Set NotePos
    global leftNoteCheckPos, rightNoteCheckPos
    leftNoteCheckPos = (get_canvas_width()//2 - 200,
                        get_canvas_height()//2 - 250)
    rightNoteCheckPos = (get_canvas_width()//2 + 200,
                         get_canvas_height()//2 - 250)

    # --- InputSystem
    global strokeInput
    strokeInput = InputSystem.StrokeInputSystem(
        onUpStrokeInput, onDownStokeInput)

    global downInput
    downInput = InputSystem.DownInputSystem(
        onOneDownInput, onTwoDownInput, onThreeDownInput, onFourDownInput)

    # --- bg
    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Play_Bg.png', (get_canvas_width()//2, get_canvas_height()//2)))

    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Play_NoteLine.png', (get_canvas_width()//2 - 200, get_canvas_height()//2)))

    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Play_NoteLine.png', (get_canvas_width()//2 + 200, get_canvas_height()//2)))

    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Play_InputBar.png', leftNoteCheckPos))

    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Play_InputBar.png', rightNoteCheckPos))

    # --- music
    global music
    music = gfw.load_music(gobj.resMusic(playMusicName))
    music.play()

    # --- time
    global startTime, endTime
    startTime = time.time()
    endTime = startTime + MP3(gobj.resMusic(playMusicName)).info.length

    pass


def update():
    gfw.world.update()

    global strokeInput, downInput, key_ctrl, key_s, endTime

    if inputType == 'stroke':
        strokeInput.updateInput()
        strokeInput.inputCheck()
    elif inputType == 'down':
        downInput.inputCheck()

    # --- 음악이 끝났는지 확인
    if time.time() > endTime:
        pass
    pass


def draw():
    gfw.world.draw()


def handle_event(e):
    global strokeInput, downInput, inputType, key_ctrl, key_s

    if e.type == SDL_QUIT:
        return gfw.quit()

    if e.type == SDL_KEYDOWN:
        if e.key != None and e.key >= ord('a') and e.key <= ord('z') and key_ctrl == False:
            print(str(chr(e.key - 32)) + str(time.time()))
            strokeInput.addInput(chr(e.key - 32), time.time())
            downInput.addInput(chr(e.key - 32), time.time())

        if e.key == SDLK_LCTRL:
            key_ctrl = True

        if e.key == SDLK_s:
            key_s = True

        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    if e.type == SDL_KEYUP:
        if e.key == SDLK_LCTRL:
            key_ctrl = False

        if e.key == SDLK_s:
            key_s = False
    pass


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
