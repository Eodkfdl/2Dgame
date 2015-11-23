import random

from pico2d import *

class Stage1:


    def __init__(self, w, h):
        self.image = load_image('image///mapp1.png')
        self.image2 = load_image('image///mapp1.png')
        self.bgm = load_music('sound///성당.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)


    def draw(self):
        x=int(self.left)
        w=min(self.image.w-x,self.screen_width)

        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw(0,0,self.screen_width-w,self.screen_height,w,0)



    def update(self, frame_time):
        self.left = (self.left+frame_time * self.speed)% self.image.w


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key== SDLK_LEFT:self.speed -= Stage1.SCROLL_SPEED_PPS
            elif event.key== SDLK_RIGHT:self.speed += Stage1.SCROLL_SPEED_PPS


        if event.type == SDL_KEYUP:
            if event.key== SDLK_LEFT:self.speed += Stage1.SCROLL_SPEED_PPS
            elif event.key== SDLK_RIGHT:self.speed -= Stage1.SCROLL_SPEED_PPS

    def __del__(self):
        del self.image
        del self.bgm
