import random
import json
import os
import math
import game_framework
import title_state

from pico2d import *



name = "MainState"
windowsizex,windowsizey=800,600
boy = None
tvx=1
brick = None
font = None
tearscount=0

pause=1
def enter():
    global player,brick,hold,bg,tears,tvx,monster1
    monster1=Monster1()
    tears = []
    tvx=1
    hold=Hold()
    player = Player()
    brick = Brick()
    bg=Background()
class Hold:
    def __init__(self):
        self.image = load_image('hold.png')

    def draw(self):
        self.image.draw(400, 30)


class Brick:
    def __init__(self):
        self.image = load_image('brick.png')

    def draw(self):
        self.image.draw(400, 30,800,150)
class Background:
    def __init__(self):
        self.image=load_image('mapb1.png')

    def draw(self):
        self.image.draw(400,300,windowsizex,windowsizey)

def Crush(Ob1,Ob2):
    if (abs(Ob1.x-Ob2.x)<20 and abs(Ob1.y-Ob2.y)<10):
        return 1
    else:
        return 0
class Monster1 :
    image = None

    def __init__(self):
        self.x, self.y = 500,150
        self.crush=0
        self.frame = 0
        if Monster1.image == None:
            Monster1.image = load_image('monster1.png')

    def draw(self):
        self.image.clip_draw(self.frame * 32, 0, 30, 64, self.x, self.y,80,120)
    def update(self):
       self.frame=(self.frame+1)%3


class Player:
    image = None
    global Tearsx,Tearesy,tvx
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND= 0, 1, 2, 3
    RL= 3;


    def handle_left_run(self):
        self.x -= 10
        self.RL = 2


    def handle_left_stand(self):
        self.run_frame+=1


    def handle_right_run(self):
        self.RL = 3
        self.x += 10



    def handle_right_stand(self):
        self.run_frame+=1

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
    }


    def update(self):
        if(self.state<2):
            self.frame = (self.frame + 1) % 5
        if(self.state>1):
            self.frame=0

        if(self.Jumpstat==1):
            self.jump+=1
            if (self.jump<7) :
                self.y+=10
            if (self.jump>7) :
                self.y-=10

            if (self.jump==13) :
                self.Jumpstat=0
                self.jump=0


        self.handle_state[self.state](self)



    def __init__(self):
        self.x, self.y = 120, 120
        self.frame = 0
        self.state = self.RIGHT_STAND
        self.jump =0
        self.Jumpstat=0
        self.RL=3
        self.run_frame=0
        if Player.image == None:
            Player.image = load_image('isaac.png')

    def draw(self):
        self.image.clip_draw(self.frame * 30, self.RL * 35, 30, 35, self.x, self.y,60,60)


class Tears:
    image = None
    global tvx
    def __init__(self):
        self.x, self.y = player.Tearsx,player.Tearsy
        self.crush=0
        self.frame = 0
        self.tvx = tvx
        self.rd=0
        self.pi=3.141592
        if Tears.image == None:
            Tears.image = load_image('tears.png')
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 32, self.x, self.y,30,40)
    def update(self):
        self.rd+=1
        self.x += self.tvx*15 + math.cos(self.rd)
        self.y -= 5*math.sin(self.rd)

def handle_events():
    global running,tvx
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        if event.type == SDL_KEYDOWN and event.key== SDLK_RIGHT:
                player.state = player.RIGHT_RUN
                tvx=1
        if event.type == SDL_KEYUP and event.key== SDLK_RIGHT:
                 if(player.state==player.RIGHT_RUN):
                    player.state = player.RIGHT_STAND

        if event.type == SDL_KEYDOWN and event.key==SDLK_LEFT:
                player.state = player.LEFT_RUN
                tvx=-1
        if event.type == SDL_KEYUP and event.key== SDLK_LEFT :
                if(player.state==player.LEFT_RUN):
                     player.state = player.LEFT_STAND

        if event.type== SDL_KEYDOWN and event.key== SDLK_SPACE:
                player.Tearsx = player.x+(10*tvx)
                player.Tearsy = player.y+20
                tears.append(Tears())

        if event.type==SDL_KEYUP and event.key== SDLK_a and player.Jumpstat==0:
            player.Jumpstat=1

        if event.type == SDL_KEYDOWN and event.key == SDLK_h:
            pause=pause*-1

def update():
    if pause==1:
        player.update()

        for member in tears:
            member.update()
        delay(0.04);
        monster1.update()

def draw():
    if pause==-1:
        hold.draw()
    clear_canvas()
    bg.draw()
    brick.draw()
    player.draw()
    monster1.draw()
    for member in tears:
        member.draw()
    update_canvas()








