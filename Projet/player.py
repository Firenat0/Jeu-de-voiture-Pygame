import pygame
import pytmx
import pyscroll

class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('sprit 3.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x,y]
        self.images = {
            'high': self.get_image(0,0),
            'left': self.get_image(0,110),
            'right': self.get_image(0,55)
        }
        self.hitbox = pygame.Rect(0,0, self.rect.width, self.rect.height)
        self.last_position = self.position.copy()
        self.speed = 8
        self.speed_high = 4

    def speed(self,speed):
        self.speed_high = speed

    def location(self):
        self.last_position = self.position.copy()

    def change_animation(self,name):
        self.image = self.images[name]
        self.image.set_colorkey((0,0,0))

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_high(self):
        self.position[1] -= self.speed_high

    def move_down(self):
        self.position[1] += self.speed_high +0.5

    def update(self):
        self.rect.topleft = self.position
        self.hitbox = self.rect

    def move_back(self):
        self.position = self.last_position
        self.rect.topleft = self.position
        self.hitbox = self.rect

    def get_image(self, x, y):
        image = pygame.Surface([55,55])
        image.blit(self.sprite_sheet, (0,0), (x,y,55,55))
        return image