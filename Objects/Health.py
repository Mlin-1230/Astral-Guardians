import pygame

from settings.config import *
from settings.load_image import Health_img

class Health1(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[0], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx += 0
        self.rect.centery += 4
class Health2(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[1], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx += 3
        self.rect.centery += 3
class Health3(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[2], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx += 4
        self.rect.centery += 0
class Health4(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[3], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx += 3
        self.rect.centery -= 3
class Health5(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[4], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx += 0
        self.rect.centery -= 4
class Health6(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[5], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx -= 3
        self.rect.centery -= 3
class Health7(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[6], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx -= 4
        self.rect.centery += 0
class Health8(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Health_img[7], (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.health = 2
    def update(self):
        self.rect.centerx -= 3
        self.rect.centery += 3