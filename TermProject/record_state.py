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
recordMusicName = "ACDC - You Shook Me All Night Long.mp3"
music = None

# --- MusicTime
startTime = 0
endTime = 0

# --- Note
inputTypeDownImage = None
inputTypeStrokeImage = None
leftNoteInitialPos = 0
rightNoteInitialPos = 0

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


def save_record():
    global inputList, font

    # --- 파일 생성 후 저장
    content = json.dumps(inputList)
    fileName = recordMusicName[:].replace(".mp3", ".jfr")
    file = open(gobj.resMusic(fileName), 'w')
    file.write(content)
    file.close()
    print('저장')
    # --- 세이브 안내
    gfw.world.add(gfw.layer.note, textAlert(
        font, 'Record File Saved', 150, 600, 200, 200, 5))


def onOneDownInput():
    gfw.world.add(gfw.layer.note, note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '1'))
    inputList.append([inputTime(), '1'])
    pass


def onTwoDownInput():
    gfw.world.add(gfw.layer.note, note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '2'))
    inputList.append([inputTime(), '2'])
    pass


def onThreeDownInput():
    gfw.world.add(gfw.layer.note, note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '3'))
    inputList.append([inputTime(), '3'])
    pass


def onFourDownInput():
    gfw.world.add(gfw.layer.note, note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '4'))
    inputList.append([inputTime(), '4'])
    pass


def onUpStrokeInput():
    gfw.world.add(gfw.layer.note, note(
        rightNoteInitialPos[0], rightNoteInitialPos[1], 200, 'up'))
    inputList.append([inputTime(), 'up'])


def onDownStokeInput():
    gfw.world.add(gfw.layer.note, note(
        rightNoteInitialPos[0], rightNoteInitialPos[1], 200, 'down'))
    inputList.append([inputTime(), 'down'])


def enter():
    gfw.world.init(['bg', 'note', 'ui'])

    # --- Resource
    global font
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 40)

    # --- Set NotePos
    global leftNoteInitialPos, rightNoteInitialPos
    leftNoteInitialPos = (get_canvas_width()//2 - 200,
                          get_canvas_height()//2 - 250)
    rightNoteInitialPos = (get_canvas_width()//2 + 200,
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
        '/Play_InputBar.png', leftNoteInitialPos))

    gfw.world.add(gfw.layer.bg, gobj.ImageObject(
        '/Play_InputBar.png', rightNoteInitialPos))

    # --- music
    global music
    music = gfw.load_music(gobj.resMusic(recordMusicName))
    music.play()

    # --- time
    global startTime, endTime
    startTime = time.time()
    endTime = startTime + MP3(gobj.resMusic(recordMusicName)).info.length

    # --- inputType Image
    global inputTypeDownImage, inputTypeStrokeImage
    inputTypeDownImage = load_image(gobj.res('Record_KeyDown.png'))
    inputTypeStrokeImage = load_image(gobj.res('Record_KeyStroke.png'))
    inputTypeDownImage.draw_to_origin(0, 0)
    pass


def update():
    gfw.world.update()

    global strokeInput, downInput, key_ctrl, key_s, endTime

    if inputType == 'stroke':
        strokeInput.updateInput()
        strokeInput.inputCheck()
    elif inputType == 'down':
        downInput.inputCheck()

    # --- 저장 확인
    if key_ctrl == True and key_s == True:
        save_record()
        key_ctrl = False
        key_s = False

    # --- 음악이 끝났는지 확인
    if time.time() > endTime:
        save_record()
        gfw.pop()
    pass


def draw():
    gfw.world.draw()

    global inputTypeDownImage, inputTypeStrokeImage
    if inputType == 'down':
        inputTypeDownImage.draw_to_origin(0, 0)
    else:
        inputTypeStrokeImage.draw_to_origin(0, 0)
    pass


def handle_event(e):
    global strokeInput, downInput, inputType, key_ctrl, key_s

    if e.type == SDL_QUIT:
        return gfw.quit()

    if e.type == SDL_KEYDOWN:
        if e.key != None and e.key >= ord('a') and e.key <= ord('z') and key_ctrl == False:
            if inputType == 'stroke':
                print(str(chr(e.key - 32)) + str(time.time()))
                strokeInput.addInput(chr(e.key - 32), time.time())
            elif inputType == 'down':
                print(str(chr(e.key - 32)) + str(time.time()))
                downInput.addInput(chr(e.key - 32), time.time())

        if e.key == SDLK_TAB:
            if inputType == 'down':
                inputType = 'stroke'
            else:
                inputType = 'down'

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
