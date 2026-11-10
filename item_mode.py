import game_framework
from pico2d import *


def init():
    pass


def finish():
    pass


def pause():
    pass


def resume():
    pass


def update():
    import play_mode
    play_mode.update()


def render():
    import play_mode
    clear_canvas()
    play_mode.render_scene()
    update_canvas()


def handle_events():
    import play_mode

    for event in get_events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_0:
            play_mode.select_ball(None)
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mode.select_ball('small')
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mode.select_ball('large')
            game_framework.pop_mode()
        else:
            play_mode.handle_event(event)
