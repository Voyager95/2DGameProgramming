import random
import time
from pico2d import *
import gfw
import gobj
import InputSystem
from Note import Note
from mutagen.mp3 import MP3

inputType = "stroke"
recordMusicName = "ACDC - You Shook Me All Night Long.mp3"

startTime = 0
endTime = 0

leftNoteInitialPos = 0
rightNoteInitialPos = 0


def onOneDownInput():
    gfw.world.add(gfw.layer.note, Note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '1'))
    pass


def onTwoDownInput():
    gfw.world.add(gfw.layer.note, Note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '2'))
    pass


def onThreeDownInput():
    gfw.world.add(gfw.layer.note, Note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '3'))
    pass


def onFourDownInput():
    gfw.world.add(gfw.layer.note, Note(
        leftNoteInitialPos[0], leftNoteInitialPos[1], 200, '4'))
    pass


def onUpStrokeInput():
    gfw.world.add(gfw.layer.note, Note(
        rightNoteInitialPos[0], rightNoteInitialPos[1], 200, 'up'))


def onDownStokeInput():
    gfw.world.add(gfw.layer.note, Note(
        rightNoteInitialPos[0], rightNoteInitialPos[1], 200, 'down'))


def enter():
    gfw.world.init(['bg', 'note', 'ui'])

    global leftNoteInitialPos, rightNoteInitialPos
    leftNoteInitialPos = (get_canvas_width()//2 - 200,
                          get_canvas_height()//2 - 250)
    rightNoteInitialPos = (get_canvas_width()//2 + 200,
                           get_canvas_height()//2 - 250)

    global strokeInput
    strokeInput = InputSystem.StrokeInputSystem(
        onUpStrokeInput, onDownStokeInput)

    global downInput
    downInput = InputSystem.DownInputSystem(
        onOneDownInput, onTwoDownInput, onThreeDownInput, onFourDownInput)

    # bg
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

    # music
    global music
    music = gfw.load_music(gobj.resMusic(recordMusicName))
    music.play()

    # time
    startTime = time.time()
    endTime = startTime + MP3(gobj.resMusic(recordMusicName)).info.length

    # inputType Image
    global inputTypeDownImage, inputTypeStrokeImage
    inputTypeDownImage = load_image(gobj.res('Record_KeyDown.png'))
    inputTypeStrokeImage = load_image(gobj.res('Record_KeyStroke.png'))
    inputTypeDownImage.draw_to_origin(0, 0)
    pass


def update():
    gfw.world.update()

    global strokeInput, downInput

    if inputType == 'stroke':
        strokeInput.updateInput()
        strokeInput.inputCheck()
    elif inputType == 'down':
        downInput.inputCheck()
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
    global strokeInput, downInput, inputType

    if e.type == SDL_QUIT:
        return gfw.quit()

    if e.type == SDL_KEYDOWN:
        if e.key != None and e.key >= ord('a') and e.key <= ord('z'):
            if inputType == 'stroke':
                strokeInput.addInput(chr(e.key - 32), time.time())
            elif inputType == 'down':
                print(str(chr(e.key - 32)) + str(time.time()))
                downInput.addInput(chr(e.key - 32), time.time())

        if e.key == SDLK_TAB:
            if inputType == 'down':
                inputType = 'stroke'
            else:
                inputType = 'down'
    pass


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
