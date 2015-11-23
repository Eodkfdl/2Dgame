from pico2d import *

import game_framework
from tears import Tears
from background import Stage1
from player import Player
from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass



name = "main_state"
tears=None
boy = None
balls = None
big_balls = None
grass = None
background=None
def create_world():
    global boy, grass, balls,background,player,tears
    player=Player()
    tears = []
    background = Stage1(800,600)
    big_balls = [BigBall() for i in range(10)]
    balls = [Ball() for i in range(10)]
    balls = big_balls + balls



def destroy_world():
    global boy, balls, grass,background

    del(background)
    del(balls)




def enter():
    open_canvas(800,600)
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                player.handle_event(event)
        if event.type==SDL_KEYDOWN and event.key== SDLK_SPACE:

             player.Tearsy = player.y+20
             if player.state in (player.RIGHT_STAND, player.RIGHT_RUN):
                player.Tearsx = player.x+(10*player.dir)
                tears.append(Tears(player.Tearsx,player.Tearsy,1))

             if player.state in (player.LEFT_STAND, player.LEFT_RUN):
                 player.Tearsx = player.x+(10*player.dir)
                 tears.append(Tears(player.Tearsx,player.Tearsy,-1))





def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    player.update(frame_time)
    for member in tears:
            member.update(frame_time)
    background.update(frame_time)
  #  for ball in balls:
   #     if collide(boy, ball):
    #        balls.remove(ball)
     #       boy.eat(ball)



def draw(frame_time):
    clear_canvas()
    background.draw()
    player.draw_bb()
    player.draw()

    for member in tears:
        member.draw()

    update_canvas()






