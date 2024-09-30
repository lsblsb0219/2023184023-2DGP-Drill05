from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('character_move.png')

def handle_events():
    global running, dir1, dir2, onoff, wasd, start
    # running 달리기 상태
    # onoff 실행, 종료
    # wasd = 0(상) 1(좌) 2(하) 3(우)
    # start 처음 클리어 캔버스를 무시하기 위해 -> 시작 시 캐릭터 보이게 하기 위함

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            onoff = False
        elif event.type == SDL_KEYDOWN:
            running = True
            if event.key == SDLK_UP:
                dir1 += 1
                wasd = 0
            elif event.key == SDLK_LEFT:
                dir2 -= 1
                wasd = 1
            elif event.key == SDLK_DOWN:
                dir1 -= 1
                wasd = 2
            elif event.key == SDLK_RIGHT:
                dir2 += 1
                wasd = 3
            elif event.key == SDLK_ESCAPE:
                onoff = False
        elif event.type == SDL_KEYUP:
            running = False
            if event.key == SDLK_UP:
                dir1 -= 1
            elif event.key == SDLK_LEFT:
                dir2 += 1
            elif event.key == SDLK_DOWN:
                dir1 += 1
            elif event.key == SDLK_RIGHT:
                dir2 -= 1

running = False
onoff = True
start = False
x = 800 // 2
y = 600 // 2
frame = 0
dir1 = 0
dir2 = 0
wasd = 4

clear_canvas()
background.draw(400, 300, 800, 600)
character.clip_draw(5 * 100, 300, 100, 100, x, y, 80, 80)
update_canvas()

while onoff:
    if start == True:
        clear_canvas()
        background.draw(400, 300, 800, 600)

    if running:
        start = True
        if wasd == 0:
            if y + dir1 * 5 >= 10 and y + dir1 * 5 <= 600:
                character.clip_draw(frame * 100, 0, 100, 100, x, y, 80, 80)
                y += dir1 * 5
            else:
                character.clip_draw(frame * 100, 0, 100, 100, x, y, 80, 80)
        elif wasd == 1:
            if x + dir2 * 5 >= 10 and x + dir2 * 5 <= 800:
                character.clip_draw(frame * 100, 200, 100, 100, x, y, 80, 80)
                x += dir2 * 5
            else:
                character.clip_draw(frame * 100, 200, 100, 100, x, y, 80, 80)
        elif wasd == 2:
            if y + dir1 * 5 >= 10 and y + dir1 * 5 <= 600:
                character.clip_draw(frame * 100, 300, 100, 100, x, y, 80, 80)
                y += dir1 * 5
            else:
                character.clip_draw(frame * 100, 300, 100, 100, x, y, 80, 80)
        elif wasd == 3:
            if x + dir2 * 5 >= 10 and x + dir2 * 5 <= 800:
                character.clip_draw(frame * 100, 100, 100, 100, x, y, 80, 80)
                x += dir2 * 5
            else:
                character.clip_draw(frame * 100, 100, 100, 100, x, y, 80, 80)
        frame = (frame + 1) % 6
    else:
        if wasd == 0:
            character.clip_draw(frame * 100, 0, 100, 100, x, y, 80, 80)
        elif wasd == 1:
            character.clip_draw(frame * 100, 200, 100, 100, x, y, 80, 80)
        elif wasd == 2:
            character.clip_draw(frame * 100, 300, 100, 100, x, y, 80, 80)
        elif wasd == 3:
            character.clip_draw(frame * 100, 100, 100, 100, x, y, 80, 80)

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()