import random

from pico2d import *

class Player:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    eat_sound = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.RL=3
        self.state = self.RIGHT_STAND
        self.eatn=0
        self.jump =0
        self.Jumpstat=0
        self.Tearsx=0
        self.Tearsy=0
        if Player.image == None:
            Player.image = load_image('image\\isaac.png')
        if Player.eat_sound == None:
            Player.eat_sound = load_wav('sound\\/탬습득.wav')
            Player.eat_sound.set_volume(128)

    def eat(self, ball):
        self.eat_sound.play()
        self.eatn=1
    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        if self.eatn == 0:
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN):
                pass #self.bgm.play()
        self.eatn = 0

        self.life_time += frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        if(self.dir!=0):
         self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        if(self.dir==0):
            self.total_frames = 0

        self.frame = int(self.total_frames) % 5

        self.x += (self.dir * distance)

        self.x = clamp(0, self.x, 800)#맵밖으로 못나가게 하는거

        if(self.Jumpstat==1):
            self.jump+=1
            if (self.jump<70) :
                self.y+=1
            if (self.jump>70) :
                self.y-=1

            if (self.jump==139) :
                self.Jumpstat=0
                self.jump=0
    def draw(self):
        self.image.clip_draw(self.frame * 30, self.RL * 35, 30, 35, self.x, self.y,60,60)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 35, self.x + 30, self.y + 35

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
                self.RL=2
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                self.dir = 1
                self.RL=3
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir = 0
        if event.type==SDL_KEYUP and event.key== SDLK_a and self.Jumpstat==0:
            self.Jumpstat=1