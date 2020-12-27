import pygame as pg
#from sprite import Player
import sys

class Player:
    def __init__(self):
        #pg.sprite.Sprite.__init__(self)
        self.image_width = 50; self.image_height=50
        self.image=pg.Surface((self.image_width, self.image_height))
        self.image.fill((200,0,0))
        self.image_rect=self.image.get_rect()#will appear in upper left of screen
        self.image_rect.x=150; self.image_rect.y=100
        #self.speedx=0; self.speedy=0
        
        
    def move(self): ...
        
    def update(self): ...


class Game:
    def __init__(self):
        pg.init()
        self.screen_width=500; self.screen_height=500
        self.colors={"color1": (100,100,100), "color2": (150, 0,0)}
        self.screen=pg.display.set_mode((self.screen_width, self.screen_height))
        self.clock=pg.time.Clock()
        #self.player=Player()#Game is a composite

    def display_game(self):
        while True:
            self.clock.tick(15)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
            self.screen.fill(self.colors["color1"])#put in a color
            #self.screen.blit(self.player.image, (100, 100))
            pg.display.flip()

game=Game()
game.display_game()

