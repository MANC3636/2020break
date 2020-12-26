import pygame as pg

class Player (pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_width = 50; self.image_height=50
        self.image=pg.Surface((self.image_width, self.image_height))
        self.image.fill((200,0,0))
        self.image_rect=self.image.get_rect()#will appear in upper left of screen
        self.image_rect.x=100; self.image_rect.y=100
        self.speedx=0; self.speedy=0
