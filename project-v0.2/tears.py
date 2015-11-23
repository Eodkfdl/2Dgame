import random
import player
from pico2d import *


class Tears:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self,tearsx,tearsy,dir):
        self.x, self.y = tearsx,tearsy
        self.crush=0
        self.frame = 0
        self.tvx=dir
        self.rd=0
        self.pi=3.141592
        if Tears.image == None:
            Tears.image = load_image('image///tears.png')
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 32, self.x, self.y,30,40)
    def update(self,frame_time):
        self.rd+=1
        distance = Tears.RUN_SPEED_PPS * frame_time
        self.x += self.tvx*frame_time*500 + math.cos(self.rd)
        self.y -= 5*math.sin(self.rd)