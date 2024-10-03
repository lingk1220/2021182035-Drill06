from random import random, randint
from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')


character = load_image('animation_sheet.png')


def handle_events():
    global running


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def run_destination():
    global pos_character, destination, f

    if 1 > get_dist(pos_character, destination):
        pos_character[0] = destination[0]
        pos_character[1] = destination[1]
        reset_destination()
    else:
        dx = (destination[0] - pos_character[0])
        dy = (destination[1] - pos_character[1])

        if(dx > 0): f = ''
        else: f = 'h'


        pos_character[0] += dx / 30
        pos_character[1] += dy / 30

        pass


def get_dist(pos_character, destination):
    cx, cy = pos_character[0], pos_character[1]
    dx, dy = destination[0], destination[1]
    return math.sqrt(math.pow(dx - cx, 2) + math.pow(dy - cy, 2))

def reset_destination():
    destination[0] = randint(10, TUK_WIDTH - 10 + 1)
    destination[1] = randint(10, TUK_HEIGHT - 10 + 1)

    pass

running = True
frame = 0
pos_character = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
destination = [0, 0]
reset_destination()

hide_cursor()

f = ''

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(destination[0], destination[1])
    character.clip_composite_draw(frame*100, 100 * 1, 100, 100, 0, f, pos_character[0], pos_character[1], 100, 100)
    update_canvas()

    run_destination()

    frame = (frame + 1) % 8
    delay(0.01)
    handle_events()


close_canvas()




