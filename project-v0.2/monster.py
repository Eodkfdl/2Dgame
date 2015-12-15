import random
import game_framework
from pico2d import *
class Gate:
    image = None

    def __init__(self,x,y):
        self.x, self.y = x,y+60
        self.spoty=y
        self.frame = 0
        self.frame2 = 0.0
        self.realx=0
        self.clear=0
        self.quit=0
        self.clearimg2=load_image('image///death.png')
        self.clearimg=load_image('image///black.png')
        if Gate.image == None:
           Gate.image = load_image('image///gate.png')
    def update(self,frame_time):
        if(self.clear>1):
         self.quit+=1
        if(self.quit>100):
                game_framework.quit()
    def draw(self,camx):
        if (self.clear==1):
            self.clearimg.clip_draw(0,0,800,400,400,300,800,600)
            self.clearimg2.clip_draw(0,0,59,96,400,300,800,600)
        self.image.clip_draw( self.frame*32,0 , (self.frame+1)*32, 32, self.x-camx, self.y,120,120)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 60, self.y - 60, self.realx + 60, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
class Devileye :
    image = None

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.spoty=y
        self.hp=40
        self.ydir=1
        self.frame = 0
        self.frame2 = 0.0
        self.realx=0

        if Devileye.image == None:
            Devileye.image = load_image('image///devileye.png')
    def update(self,frame_time):
        if(self.y>self.spoty+200):
            self.ydir=-1
        if(self.y<self.spoty-200):
            self.ydir=1
        self.frame2+=frame_time*50
        self.frame=int(self.frame2)%2
        self.y+=self.ydir
    def draw(self,camx):
        self.image.clip_draw( 0, 106*self.frame, 142, 106, self.x-camx, self.y,60,60)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 30, self.y - 30, self.realx + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
class Peep :
    image = None

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.hp=16
        self.xdir=1
        self.realx=0
        self.die=0
        self.spotx=x
        if Peep.image == None:
            Peep.image = load_image('image///Peep.png')
    def update(self,frame_time):
        if(self.x>self.spotx+100):
            self.xdir=-1
        if(self.x<self.spotx-100):
            self.xdir=1
        self.x+=self.xdir
        if(self.hp<0):
           self.x=0
           self.y=0
    def draw(self,camx):
        self.image.clip_draw( 0, 0, 32, 32, self.x-camx, self.y,30,30)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 30, self.y - 30, self.realx + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Ghost :
    image = None

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.hp=16
        self.xdir=1
        self.realx=0
        self.die=0
        self.spotx=x
        self.rd=0
        if Ghost.image == None:
            Ghost.image = load_image('image///ghost.png')
    def update(self,frame_time):
        self.rd+=1
        if(self.x>self.spotx+50):
            self.xdir=-1
        if(self.x<self.spotx-50):
            self.xdir=1
        self.x += self.xdir*frame_time*100 + math.cos(self.rd)
        self.y -= 10*math.sin(self.rd)
    def draw(self,camx):

        if(self.hp>8):
            self.image.clip_draw( 0, 32, 32, 64, self.x-camx, self.y,60,60)
        else:
            self.image.clip_draw( 0, 0, 32, 32, self.x-camx, self.y,60,60)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 25, self.y - 25, self.realx + 25, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
