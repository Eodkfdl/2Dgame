import random
import player
from pico2d import *


class Tears:
    image = None
    fire_sound = None

    def __init__(self,tearsx,tearsy,dir):
        self.x, self.y = tearsx,tearsy
        self.dmg=1;
        self.crush=0
        self.frame = 0
        self.framea=0
        self.tvx=dir
        self.rd=0
        self.pi=3.141592
        if Tears.image == None:
            Tears.image = load_image('image///tears.png')
        if Tears.fire_sound == None:
            Tears.fire_sound  = load_wav('sound///눈물발사 (1).wav')
            Tears.fire_sound .set_volume(64)
    def fire(self):
        self.fire_sound.play()
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 32, self.x, self.y,30,40)
    def update(self,frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        if self.frame>=1:
           self.framea+=1
           self.frame = (self.framea)%3+1

        self.rd+=1
        self.x += self.tvx*frame_time*500 + math.cos(self.rd)
        self.y -= 5*math.sin(self.rd)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

class Firetears:
    image = None
    fire_sound = None
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    def __init__(self,tearsx,tearsy,dir):

        self.x, self.y = tearsx, tearsy

        self.dmg=1;
        self.crush=0
        self.frame = 0
        self.n=0.0

        self.tvx=dir
        self.rd=0
        self.pi=3.141592
        self.rl=0
        if (dir==-1):
            self.rl=1
        if (dir==1):
            self.rl=0

        if Firetears.image == None:
            Firetears.image = load_image('image///fireteras1.png')
        if Firetears.fire_sound == None:
            Firetears.fire_sound  = load_wav('sound///눈물발사 (2).wav')
            Firetears.fire_sound .set_volume(64)

    def fire(self):
        self.fire_sound.play()
    def draw(self):
        self.image.clip_draw(self.frame * 64,self.rl*64 , 64, 64, self.x, self.y,30,40)
    def update(self,frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        self.rd+=1
        self.n += Firetears.FRAMES_PER_ACTION * Firetears.ACTION_PER_TIME * frame_time
        self.frame = int(self.n)%4
        self.x += self.tvx*frame_time*500 + math.cos(self.rd)
        #self.y -= 5*math.sin(self.rd)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7