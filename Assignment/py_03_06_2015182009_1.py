from pico2d import *
import random
from helper import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


class Boy:
    age = 10

    def __init__(self):  # __init__: 생성자 / self: 해당 인스턴스가 불려온 것

        # 위치
        self.x, self.y = random.randint(100, 700), random.randint(100, 500)

        # 이미지
        self.img = load_image('./Resources/Images/run_animation.png')
        #self.img = load_image('../res/run_animation.png')
        self.fidx = random.randint(0, 7)
        self.imgSize = 8

        # 속도
        self.speed = 0  # 현재 이동속도

        # 목적지
        self.isDestinationExist = False
        self.presentDestination = (0, 0)  # 목적지
        self.destinations = []  # 목적지 예정 리스트

    def draw(self):
        self.img.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)

    def update(self):

        # 목적지가 있는지 확인합니다. 만약 없다면 목적지 예정 리스트에서 찾아서 추가합니다. * 없는 경우 캐릭터를 멈춥니다.
        if self.isDestinationExist == False:
            if len(self.destinations) > 0:
                self.isDestinationExist = True
                self.presentDestination = self.destinations.pop(0)
                print("다음 목적지: " + str(self.presentDestination))
                if self.speed == 0:
                    self.speed = 1
            else:
                self.speed = 0

        # 목적지가 있다면 움직입니다. 목적지가 없는 경우 목적지 플레그를 변경합니다.
        if self.isDestinationExist == True:
            dx, dy = delta((self.x, self.y),
                           self.presentDestination, self.speed)
            #print(dx, dy)
            pos, done = move_toward(
                (self.x, self.y), (dx, dy), self.presentDestination)
            self.x = pos[0]
            self.y = pos[1]

            if done == True:
                self.speed = 0
                self.isDestinationExist = False
                self.fidx = 0

        # 애니메이션을 최신화합니다.
        if self.speed != 0:
            self.fidx = (self.fidx + 1) % self.imgSize

    def addDestination(self, target):

        self.destinations.append(target)

    def addSpeed(self):
        if self.isDestinationExist == True:
            self.speed += 1


class Grass:
    def __init__(self):
        self.x, self.y = 400, 30
        self.img = load_image('./Resources/Images/grass.png')
        #self.img = load_image('../res/grass.png')

    def draw(self):
        self.img.draw(self.x, self.y)


def handle_events(boy):
    global running
    # 마우스 입력
    x, y = 0, 0
    rightButtonDown, leftButtonDown = False, False

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:   # 왼쪽 버튼
                leftButtonDown = True
                x = event.x
                y = KPU_HEIGHT - 1 - event.y
            elif event.button == 3:  # 오른쪽 버튼
                rightButtonDown = True

    if leftButtonDown == True:
        boy.addDestination((x, y))

    if rightButtonDown == True:
        boy.addSpeed()


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# 객체 생성

boy = Boy()
grass1 = Grass()
grass2 = Grass()
grass2.x = 900
# 루프

running = True
while(running):
    clear_canvas()  # Game Rendering

    grass1.draw()
    grass2.draw()

    boy.draw()

    update_canvas()

    handle_events(boy)  # Game Logic

    boy.update()

    delay(.01)


close_canvas()
