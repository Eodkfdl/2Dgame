import random

from pico2d import *

class Devileye :
    image = None

    def __init__(self,x):
        self.x, self.y = x,150
        self.hp=4
        self.ydir=1
        self.frame = 0
        self.frame2 = 0.0
        self.realx=0
        if Devileye.image == None:
            Devileye.image = load_image('image///devileye.png')
    def update(self,frame_time):
        if(self.y>400):
            self.ydir=-1
        if(self.y<100):
            self.ydir=1
        self.frame2+=frame_time*50
        self.frame=int(self.frame2)%2
        self.y+=self.ydir
        if(self.hp<0):
           self.x=0
           self.y=0
    def draw(self,camx):
        self.image.clip_draw( 0, 106*self.frame, 142, 106, self.x-camx, self.y,60,60)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 30, self.y - 30, self.realx + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

