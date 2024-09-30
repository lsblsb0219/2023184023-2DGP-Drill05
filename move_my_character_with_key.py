from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('character_move.png')

def handle_events():
    global running, dir1, dir2, onoff, wasd
    # wasd = 0(상) 1(좌) 2(하) 3(우)

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            onoff = False
        elif event.type == SDL_KEYDOWN:
            running = True

        elif event.type == SDL_KEYUP:
            running = False

running = False
onoff = True
x = 800 // 2
y = 600 // 2
frame = 0
dir1 = 0
dir2 = 0
wasd = 4

while onoff:
    clear_canvas()
    background.draw(400, 300, 800, 600)

    if running:
        pass
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()