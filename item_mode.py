import game_framework
from pico2d import *


small_ball = None
large_ball = None
font = None


def init():
    global small_ball, large_ball, font
    small_ball = load_image('ball21x21.png')
    large_ball = load_image('ball41x41.png')
    font = load_font(r'C:\Windows\Fonts\arial.ttf', 24)


def finish():
    global small_ball, large_ball, font
    small_ball = None
    large_ball = None
    font = None


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
    render_selection()
    update_canvas()


def render_selection():
    import play_mode

    selected = play_mode.boy.ball_size
    options = (
        (280, None, '0: NONE', selected is None),
        (400, small_ball, '1: SMALL', selected == 'small'),
        (520, large_ball, '2: LARGE', selected == 'large'),
    )

    for x, image, label, is_selected in options:
        if image is not None:
            image.draw(x, 330)
        font.draw(x - 45, 270, label, (255, 255, 255))
        if is_selected:
            draw_rectangle(x - 50, 295, x + 50, 365)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            continue
        else:
            play_mode.handle_event(event)
