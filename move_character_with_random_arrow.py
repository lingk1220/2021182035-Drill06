from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')



character = load_image('animation_sheet.png')


def handle_events():
    global running

    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def run_destination():
    global pos_character, destination

    if 1 > get_dist(pos_character, destination):
        pos_character = destination
        reset_destination()
    else:
        pos_character[0] += (destination[0] - pos_character[0]) / 30
        pos_character[1] += (destination[1] - pos_character[1]) / 30

        pass


def get_dist(pos_character, destination):
    cx, cy = pos_character[0], pos_character[1]
    dx, dy = destination[0], destination[1]
    return math.sqrt(math.pow(dx - cx, 2) + math.pow(dy - cy, 2))

def reset_destination():
    pass

running = True
frame = 0
pos_character = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
destination = [1000, 10]

hide_cursor()


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, pos_character[0], pos_character[1])
    update_canvas()
    run_destination()
    frame = (frame + 1) % 8
    delay(0.01)
    handle_events()


close_canvas()




