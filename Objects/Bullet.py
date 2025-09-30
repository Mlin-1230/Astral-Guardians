import pygame

from settings.config import *
from settings.load_image import Bullet15_img, Bullet26_img, Bullet37_img, Bullet48_img

#子彈
class Bullet1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet15_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 8
        self.speedx = 0
    def update(self):
        self.rect.y -= self.speedy
        self.rect.x += self.speedx
        if self.rect.centery <= 500:
            self.kill()

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet26_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 6
        self.speedx = 6
    def update(self):
        self.rect.y -= self.speedy
        self.rect.x -= self.speedx
        if self.rect.centerx <= 600:
            self.kill()

class Bullet3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet37_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 0
        self.speedx = 8
    def update(self):
        self.rect.y += self.speedy
        self.rect.x -= self.speedx
        if self.rect.centerx <= 600:
            self.kill()

class Bullet4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet48_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 6
        self.speedx = 6
    def update(self):
        self.rect.y += self.speedy
        self.rect.x -= self.speedx
        if self.rect.centerx <= 600:
            self.kill()

class Bullet5(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet15_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 8
        self.speedx = 0
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.centery >= 500:
            self.kill()

class Bullet6(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet26_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 6
        self.speedx = 6
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.centerx >= 600:
            self.kill()

class Bullet7(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet37_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 0
        self.speedx = 8
    def update(self):
        self.rect.y -= self.speedy
        self.rect.x += self.speedx
        if self.rect.centerx >= 600:
            self.kill()

class Bullet8(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Bullet48_img, (75, 75))
        self.image.set_colorkey(BLACK)
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y+50
        self.speedy = 6
        self.speedx = 6
    def update(self):
        self.rect.y -= self.speedy
        self.rect.x += self.speedx
        if self.rect.centerx >= 600:
            self.kill()