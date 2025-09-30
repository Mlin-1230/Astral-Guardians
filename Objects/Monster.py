import pygame

from settings.load_image import Monster_anim

#怪物
class Monster1(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx += 0
        self.rect.centery += 4
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster2(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx += 3
        self.rect.centery += 3
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster3(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx += 4
        self.rect.centery += 0
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster4(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx += 3
        self.rect.centery -= 3
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster5(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx += 0
        self.rect.centery -= 4
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster6(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx -= 3
        self.rect.centery -= 3
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster7(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx -= 4
        self.rect.centery += 0
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center
class Monster8(pygame.sprite.Sprite):
    def __init__(self, center, number):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.image = Monster_anim[self.number][0]
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
    def update(self):
        self.rect.centerx -= 3
        self.rect.centery += 3
        now = pygame.time.get_ticks()
        if now-self.frame_rate > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
            else:
                self.image = Monster_anim[self.number][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center