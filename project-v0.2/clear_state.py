from pico2d import *
import main_state
import game_framework

name = "ClearState"
image = None


def enter():
    global image3,image2
    image3=load_image('image///clear.png')
    image2=load_image('image///black.png')

def exit():
    global image3
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key)==(SDL_KEYDOWN, SDLK_SPACE):
                game_framework.quit()
def draw(frame_time):
    clear_canvas()
    image3.draw(400,300)
    update_canvas()
