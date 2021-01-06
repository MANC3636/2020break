import pygame as pg
import settings2

pg.init()
FPS= 5
screen = pg.display.set_mode(settings2.sizes["big screen"])
clock=pg.time.Clock()
#--------------images---------------------------
little_guy=pg.Surface(settings2.sizes["avatar"])
mid_guy=pg.Surface(settings2.sizes["mid-avatar"])
big_guy=pg.Surface(settings2.sizes["big-avatar"])
#loaded_image1=pg.image.load(pics["tank1])
#----------put images into a list----------------
avatar_increase_size=[little_guy, mid_guy, big_guy]
print("len of avatar_increase_size is: ", len(avatar_increase_size))#diagnostic

class Animated():
    def __init__(self):
        self.x=200
        self.y=300
        self.anime_speed_init=10
        self.anime_speed=self.anime_speed_init
        self.anime_list=[little_guy, mid_guy, big_guy]
        self.anime_list_index_num=0
        self.image=self.anime_list[self.anime_list_index_num]
        self.anime_max=len(self.anime_list)-1#anime_max is the size of the list
        #self.update(0)

    def update(self, pos):
        if pos !=0:
            self.anime_speed-=1
            self.x+=pos
            if self.anime_speed!=0:

                self.image=self.anime_list[self.anime_list_index_num]
                if self.anime_list_index_num==self.anime_max:
                    self.anime_list_index_num=0
                else:self.anime_list_index_num+=1
        screen.blit(self.image, (self.x, self.y))

pos=0
animated_obj=Animated()#instantiate our object

#game loop------------------------------------
yellow_grapes=True
while yellow_grapes:
    clock.tick(FPS)
    screen.fill(settings2.colors["green"])
    #event management-----------------------
    for event in pg.event.get():
        if event.type==pg.QUIT:
            yellow_grapes=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                pos=1
    #update-----------------------------------
    pg.display.update()
    animated_obj.update(pos)

    #draw------------------------------------
    pg.display.flip()
pg.quit()
