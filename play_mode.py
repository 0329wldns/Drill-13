from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass
import pause_mode
import item_mode
import title_mode


def handle_events():
    event_list = get_events()
    for event in event_list:
        handle_event(event)


def handle_event(event):
    global running

    if event.type == SDL_QUIT:
        running = False
    elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        game_framework.change_mode(title_mode)
    elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
        game_framework.push_mode(pause_mode)
    elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
        game_framework.push_mode(item_mode)
    else:
        boy.handle_event(event)


def select_ball(size):
    boy.set_ball_size(size)


def init():
    global boy


    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    render_scene()
    update_canvas()


def render_scene():
    game_world.render()


def finish():
    pass


def pause():
    pass


def resume():
    pass

running = True
