from pico2d import *

WEDTH = 1920//2
HEIGHT = 690


class Bird:         # 주인공 객체
    def __init__(self):
        self.frame = 0
        self.bottom = 0                 # 상하 움직임 시 변화, 현재 적용 X
        self.x, self.y = WEDTH//2, HEIGHT//2
        self.dir_x, self.dir_y = 0, 0
        self.image = load_image('bird.png')

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5

    def draw(self):
        self.image.clip_draw(self.frame * 207, self.bottom * 203, 207, 203, self.x, self.y, 80, 80)


class Sky:      # 배경
    def __init__(self):
        self.frame = 0
        self.image = load_image('sky.png')

    def update(self):
        self.frame = (self.frame + 1) % 96

    def draw(self):
        self.image.clip_draw(self.frame * 10, 0, WEDTH, HEIGHT, WEDTH//2, HEIGHT//2)


class Enemy:
    pass


def handle_event():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                bird.dir_x -= 1
            elif event.key == SDLK_RIGHT:
                bird.dir_x += 1
            elif event.key == SDLK_UP:
                bird.dir_y += 1
            elif event.key == SDLK_DOWN:
                bird.dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                bird.dir_x += 1
            elif event.key == SDLK_RIGHT:
                bird.dir_x -= 1
            elif event.key == SDLK_UP:
                bird.dir_y -= 1
            elif event.key == SDLK_DOWN:
                bird.dir_y += 1


open_canvas()

bird = Bird()
sky = Sky()
running = True

while running:
    handle_event()

    sky.update()
    bird.update()

    clear_canvas()

    sky.draw()
    bird.draw()

    update_canvas()
    delay(0.04)

close_canvas()