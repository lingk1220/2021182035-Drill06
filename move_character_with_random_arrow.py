from pico2d import *


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

    if 5 > get_dist(pos_character, destination):
        pos_character = destination
        reset_destination()
    else:
        pos_character[0] += pos_character[0] - destination[0] // 100
        pass


def get_dist(pos_character, destination):
    return 1
    pass

def reset_destination():
    pass

running = True
frame = 0
pos_character = {TUK_WIDTH // 2, TUK_HEIGHT // 2}
destination = {600, 600}

hide_cursor()


while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, 400, 400)
    update_canvas()
    run_destination();
    pass

close_canvas()




