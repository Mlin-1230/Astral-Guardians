import pygame

from settings.load_image import Heal_anim

#治療動畫
class Heal(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = Heal_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75
    def update(self):
        now = pygame.time.get_ticks()
        if now-self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(Heal_anim):
                self.kill()
            else:
                self.image = Heal_anim[self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center