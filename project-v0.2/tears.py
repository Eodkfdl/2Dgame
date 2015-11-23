import random
import player
from pico2d import *

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