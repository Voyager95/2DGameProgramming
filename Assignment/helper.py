import math

# arguments: pos, delta, target
# - pos = (x, y) tuple
# - delta = (dx, dy) tuple
# - target = (x, y) tuple
# returns: (pos, done)
# - pos = (x, y) tuple
# - done = True if arrived


def move_toward(pos, delta, target):
    done = False
    x, y = pos[0] + delta[0], pos[1] + delta[1]  # 델타 값을 더해줌

    # 델타값이 양수이냐 음수이냐에 따라서 도달 여부 판단이 달라진다.
    if delta[0] > 0 and x >= target[0] or delta[0] < 0 and x <= target[0]:  # x좌표
        done = True
    if delta[1] > 0 and y >= target[1] or delta[1] < 0 and y <= target[1]:  # y좌표
        done = True

    # 완료플레그가 True이면 target이 pos값이 되고 False이면 델타값을 더한 x,y가 pos값이 된다.
    pos = target if done else (x, y)

    return (pos, done)  # 위치와 완료플레그를 반환

# arguments: pos, target, speed
# - pos = (x, y) tuple
# - target = (x, y) tuple
# - speed = pixels per frame
# returns: (dx, dy)
# - x/y pixels per frame


def delta(pos, target, speed):
    dx, dy = target[0] - pos[0], target[1] - pos[1]  # x축 거리, y축 거리 계산
    distance = math.sqrt(dx**2 + dy**2)  # 직선 거리 계산
    if distance == 0:
        return 0, 0  # 거리가 0이면 델타값을 0,0dmfh qusghks
    return dx * speed / distance, dy * speed / distance  # 거리로 나눔


# object version

def move_toward_obj(obj):
    if obj.target == None:
        return
    pos, done = move_toward(obj.pos, obj.delta, obj.target)
    if done:
        obj.target = None
        obj.delta = 0, 0

    obj.pos = pos  # 오브젝트에 이동 후 위치를 적용


def set_target(obj, target):
    obj.target = target
    obj.delta = 0, 0 if target is None else delta(obj.pos, target, obj.speed)
