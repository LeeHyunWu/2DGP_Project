from pico2d import *

WEDTH = 1920//2
HEIGHT = 690

def move_bird():
    global dir_x, dir_y, t
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dir_y += 1
                t = 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                t = 2
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                dir_y -= 1
                t = 0
            elif event.key == SDLK_DOWN:
                dir_y += 1
                t = 0
            elif event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1


dir_y, dir_x = 0, 0
x, y = WEDTH//2, HEIGHT//2

frame_bird = 0
frame_sky = 0

t = 0
running = True

open_canvas(WEDTH, HEIGHT)

sky = load_image('sky.png')
bird = load_image('bird.png')
enemy01 = load_image('enemy_bird_01.png')

while running:
    clear_canvas()

    sky.clip_draw(frame_sky * 10, 0, WEDTH, HEIGHT, WEDTH//2, HEIGHT//2)
    bird.clip_draw(frame_bird * 207, t * 203, 207, 203, x, y, 80, 80)

    move_bird()

    frame_bird = (frame_bird + 1) % 7
    frame_sky = (frame_sky + 1) % 96
    y = y + dir_y * 5
    x = x + dir_x * 5

    update_canvas()
    delay(0.04)

close_canvas()