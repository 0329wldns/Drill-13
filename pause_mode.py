import game_framework
from pico2d import *


font = None


def init():
    global font
    font = load_font(r"C:\Windows\Fonts\arial.ttf", 50)


def finish():
    global font
    del font


def update():
    pass


def render():
    #clear_canvas()
    font.draw(320, 300, "paused", (255, 255, 255))
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
