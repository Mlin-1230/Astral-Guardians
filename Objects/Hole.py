import pygame

from settings.config import *
from settings.load_image import Hole_anim

#中間的洞
class Hole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Hole_anim[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30
    def update(self):
        now = pygame.time.get_ticks()
        if now-self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(Hole_anim):
                self.frame = 0
            else:
                self.image = Hole_anim[self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center