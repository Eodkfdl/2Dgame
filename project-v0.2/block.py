import random

from pico2d import *

class Basic :
    image = None

    def __init__(self,x,y) :
        self.x, self.y = x,y
        self.realx=0
        if Basic.image == None:
            Basic.image = load_image('image///brick.png')
    def update(self,frame_time):
        pass

    def draw(self,camx):
        self.image.clip_draw( 0, 0, 985, 63, self.x-camx, self.y,60,60)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 30, self.y - 30, self.realx + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
class Card:
    image = None

    def __init__(self,x,y) :
        self.x, self.y = x,y
        self.realx=0
        self.rand=random.randint(1,4)
        if Card.image == None:
            Card.image = load_image('image///question.png')
    def update(self,frame_time):
        pass

    def draw(self,camx):
        self.image.clip_draw( 0, 0, 32, 32, self.x-camx, self.y,60,60)
        self.realx=self.x-camx
    def get_bb(self):
        return self.realx - 28, self.y - 28, self.realx + 28, self.y + 28
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
