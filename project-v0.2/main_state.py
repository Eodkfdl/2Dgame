from pico2d import *

import game_framework
import title_state
import start_state
import clear_state
from tears import Tears,Firetears
from background import Stage1,Heart,Item
from player import Player
from block import Basic,Card
from monster import Devileye,Peep,Ghost,Gate

windowx,windowy=800,600
name = "main_state"
tears=None
bricks=None
background=None
gamestatus=1
firetears = 0
stage=1

def create_world():
    global background,player,tears,heart,item,devileyes,bricks,peep,ghost,card,gate
    gate=[]
    devileyes=[]
    peep=[]
    ghost=[]
    bricks=[]
    card=[]

    for i in range(1,12):
        bricks.append(Basic(i*60,windowy/3-70))#바닥줄
    for i in range (15,30):
        bricks.append(Basic(i*60,windowy/3-70))
    for i in range (35,60):
        bricks.append(Basic(i*60,windowy/3-70))
    bricks.append(Basic(37*60,windowy/3-10))
    bricks.append(Basic(43*60,windowy/3-10))
    peep.append(Peep(43*60,windowy/3-10))
    for i in range (27,32):
        bricks.append(Basic(i*60,windowy/3-10))
    for i in range (30,32):
        bricks.append(Basic(i*60,windowy/3+50))
    ghost.append(Ghost(14*120,windowy/3+50))
    for i in range (31,32):
        bricks.append(Basic(i*60,windowy/3+110))
    for i in range (61,70):
        bricks.append(Basic(i*60,windowy/3-70))
    for i in range (71,73):
        bricks.append(Basic(i*60,windowy/3-70))
    ghost.append(Ghost(36*120,windowy/3-10))
    for i in range (74,74):
        bricks.append(Basic(i*60,windowy/3-70))
    for i in range (75,78):
        bricks.append(Basic(i*60,windowy/3-70))
    for i in range (79,81):
      bricks.append(Basic(i*60,windowy/3-70))
    peep.append(Peep(79*60,windowy/3-10))
    bricks.append(Basic(81*60,windowy/3-10))
    for i in range (82,95):
        bricks.append(Basic(i*60,windowy/3-70))
    for i in range (97,108):
        bricks.append(Basic(i*60,windowy/3-70))

    for i in range (100,108):
        bricks.append(Basic(i*60,windowy/3-10))
    peep.append(Peep(101*60,windowy/3+110))
    for i in range (101,108):
        bricks.append(Basic(i*60,windowy/3+50))
    for i in range (103,108):
        bricks.append(Basic(i*60,windowy/3+110))
    for i in range (106,108):
        bricks.append(Basic(i*60,windowy/3+170))
    devileyes.append(Devileye(106*60,windowy/3+170))
    bricks.append(Basic(107*60,windowy/3+230))
    for i in range (112,125):
        bricks.append(Basic(i*60,windowy/3+50))

    for i in range (128,130):
        bricks.append(Basic(i*60,windowy/3-10))
    for i in range (132,135):
        bricks.append(Basic(i*60,windowy/3-10))
    peep.append(Peep(99*60,windowy/3+50))
    bricks.append(Basic(135*60,windowy/3+50))
    for i in range (137,140):
        bricks.append(Basic(i*60,windowy/3-10))
    ghost.append(Ghost(69*120,windowy/3+50))
    for i in range (141,142):
        bricks.append(Basic(i*60,windowy/3-10))
    ghost.append(Ghost(71*120,windowy/3+50))
    bricks.append(Basic(143*60,windowy/3-10))
    bricks.append(Basic(145*60,windowy/3-10))
    devileyes.append(Devileye(144*60,windowy/3-10))
    for i in range (146,155):
        bricks.append(Basic(i*60,windowy/3-10))
        bricks.append(Basic(i*60,windowy/3+50))
    gate.append(Gate(153*60,windowy/3+50))
    for i in range(14,15 ):
        bricks.append(Basic(i*60,windowy/3-70))


    if(stage==1):
        devileyes.append(Devileye(4500,windowy/3-70))
        devileyes.append(Devileye(3000,windowy/3-70))
        devileyes.append(Devileye(2300,windowy/3-70))
        devileyes.append(Devileye(1200,windowy/3-70))
    item = Item()
    player=Player(windowy)
    heart= Heart(windowx,windowy)
    tears = []
    background = Stage1(windowx,windowy)




def destroy_world():
    global background,heart,item,devileye
    for member in tears:
        (member)
    for member in bricks:
        del(member)
    for member in devileyes:
        del(member)
    for member in peep:
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

              if(item.count==1):
                firetears=1
              if(item.count==2):
                  Heart.heartcount=3
                  player.hp=3
              if(item.count==3):
                  player.mujuck=5
                  heart.mujuck=5
              item.count=0
              print(firetears,item.count)
        if event.type==SDL_KEYDOWN and event.key == SDLK_q:
            player.mujuck=5
            heart.mujuck=5



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
    if(heart.mujuck>0):
        heart.heartcount=3


    for member in devileyes:
        member.update(frame_time)
        if collide(player,member) and player.woundstate==0:
              player.woundstate=1
              player.wound()
              heart.heartcount-=1
              player.hp-=1

    for member in peep:
        member.update(frame_time)
        if collide(player,member) and player.woundstate==0:
              player.woundstate=1
              player.wound()
              heart.heartcount-=1
              player.hp-=1
    for member in ghost:
        member.update(frame_time)
        if collide(player,member) and player.woundstate==0:
              player.woundstate=1
              player.wound()
              heart.heartcount-=1
              player.hp-=1

    background.update(frame_time)




    for member in tears:
        member.update(frame_time)
        for mem in devileyes :
            if collide(member,mem):
                mem.hp-= 1
                member.tvx=0
                member.framea=1
            if(mem.hp==0):
                devileyes.remove(mem)
                print(mem.hp)
        for mem in peep :
           if collide(member,mem):
                member.tvx=0
                member.framea=1
                mem.hp-= 1
           if(mem.hp==0):
                card.append(Card(mem.x,mem.y-10))
                peep.remove(mem)

        for mem in ghost :
           if collide(member,mem):
                mem.hp-= 2
                member.tvx=0
                member.framea=1
           if(mem.hp==0):
                card.append(Card(mem.x,mem.y-10))
                ghost.remove(mem)
        if member.frame>4 and firetears==0:
                tears.remove(member)
        if firetears==1:
            tears.remove(member)
        for mem in gate:
            if collide(member,mem):
                mem.frame+=1
            if mem.frame>5:
                mem.clear=1
    for mem in card:
        if collide(player,mem):
            item.count=mem.rand
            card.remove(mem)

    for member in  bricks:
        if collide(member,player) :
           # player.down=0
           if(player.x<member.realx+30 and player.x>member.realx-30) and player.y>member.y+30:
                player.y= clamp(member.y+60,player.y,member.y+120)
                player.Jumpstat=0
                player.jump=0

           if (player.y<member.y+30 and player.y>member.y-30) and (player.x<member.realx) :
                player.x=clamp(0,player.x,member.realx-60)

           if (player.y<member.y+30 and player.y>member.y-30) and (player.x>member.realx) :
                player.x=clamp(member.realx+60,player.x,member.realx+150)



def draw(frame_time):
    clear_canvas()
    background.draw(player.viewx)

    player.draw()


    for mem in card:
        mem.draw(player.viewx)

    for member in bricks:
        member.draw(player.viewx)

    for member in devileyes:
       member.draw(player.viewx)
    for member in peep:
       member.draw(player.viewx)

    for member in ghost:
       member.draw(player.viewx)


    for member in tears:
        member.draw()

    heart.draw(windowx,windowy)
    item.draw(windowx,windowy)
    for mem in gate:
        mem.draw(player.viewx)
       # member.draw_bb()
    update_canvas()






