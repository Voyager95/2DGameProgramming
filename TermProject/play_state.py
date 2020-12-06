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
from alert import textAlert
from alert import ImageAlert
import math

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
noteSpeed = -200
noteDistance_Bad = 25
noteDistance_Good = 15
noteDistance_Greate = 10
numOfNote = 0

# --- Input
strokeInput = None
downInput = None

# --- SpecialKey
key_ctrl, key_s = False, False

# --- Result
numOfHit = 0
isEnd = False
resultFont = None

# --- Resource
badImage = None
goodImage = None
greateImage = None


def music_end():
    global numOfHit, numOfNote, resultFont, isEnd, music
    gfw.world.add(gfw.layer.ui, gobj.ImageObject(
        'Play_Result.png', (get_canvas_width() / 2, get_canvas_height() / 2)))
    percent = numOfHit / numOfNote * 100
    gfw.world.add(gfw.layer.ui, textAlert(
        resultFont, str(percent), get_canvas_width() / 2, get_canvas_height() / 2 - 130, 300, 200, 500))

    resultMusic = load_wav(gobj.res('Bgm_Result.wav'))
    resultMusic.play(1)
    isEnd = True


def prepareNote():
    global noteSpeed, leftNoteCheckPos, rightNoteCheckPos, numOfNote
    jfrName = playMusicName[:].replace('.mp3', '.jfr')
    with open(gobj.RES_DIR + gobj.MUSIC_DIR + jfrName, 'r') as f:
        noteList = json.load(f)
    numOfNote = len(noteList)
    for n in noteList:
        height = n[0]
        if n[1] == 'up' or n[1] == 'down':
            gfw.world.add(gfw.layer.note, note(
                rightNoteCheckPos[0], rightNoteCheckPos[1] + height * (-1 * noteSpeed), noteSpeed, n[1]))
        else:
            gfw.world.add(gfw.layer.note, note(
                leftNoteCheckPos[0], leftNoteCheckPos[1] + height * (-1 * noteSpeed), noteSpeed, n[1]))
    pass


def inputTime():
    global startTime
    return time.time() - startTime


def note_hit(hitClass, noteType):
    global numOfHit, leftNoteCheckPos, rightNoteCheckPos, badImage, goodImage, greateImage
    numOfHit += 1
    pos = (0, 0)
    if noteType == 'up' or noteType == 'down':
        pos = rightNoteCheckPos
    else:
        pos = leftNoteCheckPos

    if hitClass == 'bad':
        gfw.world.add(gfw.layer.ui, ImageAlert(badImage, pos, 0.5))

    if hitClass == 'good':
        gfw.world.add(gfw.layer.ui, ImageAlert(goodImage, pos, 0.5))

    if hitClass == 'greate':
        gfw.world.add(gfw.layer.ui, ImageAlert(greateImage, pos, 0.5))
    pass


def check_Input(noteType):
    global rightNoteCheckPos, noteDistance_Bad, noteDistance_Good, noteDistance_Greate
    for note in gfw.world.objects[gfw.layer.note]:
        if note.noteType == noteType:
            inputDistance = abs(note.y - rightNoteCheckPos[1])
            if inputDistance < noteDistance_Bad:
                inputJudge = 'bad'
                if inputDistance < noteDistance_Good:
                    inputJudge = 'good'
                    if inputDistance < noteDistance_Greate:
                        inputJudge = 'greate'
                print(inputJudge)
                note_hit(inputJudge, noteType)
                gfw.world.remove(note)
                break
    pass


def onOneDownInput():
    check_Input('1')
    pass


def onTwoDownInput():
    check_Input('2')
    pass


def onThreeDownInput():
    check_Input('3')
    pass


def onFourDownInput():
    check_Input('4')
    pass


def onUpStrokeInput():
    check_Input('up')
    pass


def onDownStokeInput():
    check_Input('down')
    pass


def enter():
    gfw.world.init(['bg', 'note', 'ui'])

    # --- Resource
    global resultFont
    resultFont = gfw.font.load(gobj.res('ENCR10B.TTF'), 50)

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

    # --- Resource
    global badImage, goodImage, greateImage
    badImage = load_image(gobj.res('Score_Bad.png'))
    goodImage = load_image(gobj.res('Score_Good.png'))
    greateImage = load_image(gobj.res('Score_Greate.png'))

    # --- music
    global music
    music = gfw.load_music(gobj.resMusic(playMusicName))
    music.play()

    # --- time
    global startTime, endTime
    startTime = time.time()
    endTime = startTime + MP3(gobj.resMusic(playMusicName)).info.length

    # --- Generate Note
    prepareNote()
    pass


def update():
    gfw.world.update()

    global strokeInput, downInput, endTime, isEnd

    strokeInput.updateInput()
    strokeInput.inputCheck()
    downInput.inputCheck()

    # --- 음악이 끝났는지 확인
    if time.time() > endTime and isEnd == False:
        music_end()
    pass


def draw():
    gfw.world.draw()


def handle_event(e):
    global strokeInput, downInput, inputType, key_ctrl, key_s, isEnd

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

        if e.key == SDLK_RETURN and isEnd == True:
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
