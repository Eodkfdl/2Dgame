from pico2d import *

import game_framework
from tears import Tears,Firetears
from background import Stage1,Heart,Item
from player import Player
from boy import Boy # import Boy class from boy.py
from block import Basic
from ball import Ball, BigBall
from grass import Grass
from monster import Devileye

windowx,windowy=800,600
name = "main_state"
tears=None
bricks=None
background=None
gamestatus=1
firetears = 0
stage=1
def create_world():
    global background,player,tears,heart,item,devileyes,bricks
    devileyes=[]
    bricks=[]
    for i in range(1,100):
        bricks.append(Basic(i*60,windowy/3-60))
    if(stage==1):
        devileyes.append(Devileye(4500))
        devileyes.append(Devileye(3000))
        devileyes.append(Devileye(2300))
        devileyes.append(Devileye(1200))
    item = Item()
    player=Player(windowy)
    heart= Heart(windowx,windowy)
    tears = []
    background = Stage1(windowx,windowy)




def destroy_world():
    global background,heart,item,devileye
    for member in tears:
        del(member)
    for member in bricks:
        del(member)
    for member in devileyes:
        del(member)
    del(item)
    del(heart)
    del(background)





def enter():
    open_canvas(windowx,windowy)
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
    global firetears
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE) or player.state ==player.DIE:
                delay(1)
                game_framework.quit()
            else:
                player.handle_event(event)

        if firetears == 0:
            if event.type==SDL_KEYDOWN and event.key== SDLK_SPACE:

             player.Tearsy = player.y+20
             if player.state in (player.RIGHT_STAND, player.RIGHT_RUN):
                player.Tearsx = player.x+(10*player.dir)
                tears.append(Tears(player.Tearsx,player.Tearsy,1))

             if player.state in (player.LEFT_STAND, player.LEFT_RUN):
                 player.Tearsx = player.x+(10*player.dir)
                 tears.append(Tears(player.Tearsx,player.Tearsy,-1))
             for member in tears:
                 member.fire()

        if firetears == 1 :
          if event.type==SDL_KEYDOWN and event.key== SDLK_SPACE:
            player.Tearsy = player.y+10
            if player.state in (player.RIGHT_STAND, player.RIGHT_RUN):
               player.Tearsx = player.x+(10*player.dir)
               tears.append(Firetears(player.Tearsx,player.Tearsy,1))

            if player.state in (player.LEFT_STAND, player.LEFT_RUN):
                 player.Tearsx = player.x+(10*player.dir)
                 tears.append(Firetears(player.Tearsx,player.Tearsy,-1))
            for member in tears:
                 member.fire()

        if event.type==SDL_KEYDOWN and event.key== SDLK_s:
            if player.woundstate==0:
              player.woundstate=1
              player.wound()
              heart.heartcount-=1
              player.hp-=1


        if event.type==SDL_KEYDOWN and event.key == SDLK_d:
              item.count=0
              firetears=1
              print(firetears,item.count)



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
    for member in devileyes:
        member.update(frame_time)
        if collide(player,member) and player.woundstate==0:
              player.woundstate=1
              player.wound()
              heart.heartcount-=1
              player.hp-=1
    for member in tears:
            member.update(frame_time)
    background.update(frame_time)




    for member in tears:
        for mem in devileyes :
            if collide(member,mem):
                mem.hp-= 1
                member.frame=1
            if(mem.hp==0):

                print(mem.hp)
            if member.frame>4:
                tears.remove(member)
  #  for ball in balls:
   #     if collide(boy, ball):
    #        balls.remove(ball)
     #       boy.eat(ball)



def draw(frame_time):
    clear_canvas()
    background.draw(player.viewx)
    #player.draw_bb()
    player.draw()
    for member in bricks:
        member.draw(player.viewx)

    for member in devileyes:
       member.draw(player.viewx)
    #devileye.draw_bb()
    #ui는 맨마지막에 그린다.


    for member in tears:
        member.draw()
    heart.draw(windowx,windowy)
    item.draw(windowx,windowy)
       # member.draw_bb()
    update_canvas()






