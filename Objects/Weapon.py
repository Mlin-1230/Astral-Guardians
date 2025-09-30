import pygame

from settings.config import *
from settings.load_image import Weapon_img

#六台武器
class Weapon1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[0], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 600
        self.rect.centery = 900
class Weapon2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[1], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 900
        self.rect.centery = 800
class Weapon3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[2], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 1000
        self.rect.centery = 500
class Weapon4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[3], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 900
        self.rect.centery = 200
class Weapon5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[4], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 600
        self.rect.centery = 100
class Weapon6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[5], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 300
        self.rect.centery = 200
class Weapon7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[6], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 200
        self.rect.centery = 500
class Weapon8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Weapon_img[7], (200, 200))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 300
        self.rect.centery = 800