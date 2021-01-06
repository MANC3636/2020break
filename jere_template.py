import sys
import pygame as pg
from decorator3 import timer

class Player(pg.sprite.Sprite):#1
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)#3
        #the image
        self.image = pg.Surface((50,50))
        #self.image = pg.image.load("BenChiliBowl.png")
        self.image=pg.transform.scale(self.image, (200,200))
        #self.image.fill((0,0,20))
        #rect for the image; remember, Pygame moves the rect and the image goes along for the ride
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, (150,250,250),self.rect, 5)#rect around image
        #what follows is used to move the rect
        self.speedx=0; self.speedy=0#
        self.x = x
        self.y = y #this is tricky to explain

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.speedx = 0
        self.speedy = 0
        #collects user input
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.speedy=-4
        if keys[pg.K_DOWN]:
            self.speedy=1
        if keys[pg.K_LEFT]:
            self.speedx=-1
        if keys[pg.K_RIGHT] and self.rect.x <=100:
            self.speedx=1
        #processes user input
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx

class Run_Game:
    def __init__(self):
        self.screen=pg.display.set_mode((600,600))
        self.clock=pg.time.Clock()#
        self.goliath=Player(45, 13)
        #self.opera=scratch_28.Music("o-fortuna.mp3")
        self.all_sprites=pg.sprite.Group()#
        self.all_sprites.add(self.goliath)#

    @timer
    def gaming(self):
        pg.init()
        while True:
            self.clock.tick(20)#
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
            self.screen.fill((0,205,5))
            self.goliath.update()
            #self.opera.music_play()
            self.screen.blit(self.goliath.image,
                             self.goliath.rect)
            pg.display.flip()

game=Run_Game()
game.gaming()
