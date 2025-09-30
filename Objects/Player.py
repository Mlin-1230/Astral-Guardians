import pygame

from settings.config import *
from settings.load_image import Mark_img

from Objects.Bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.image = pygame.transform.scale(Mark_img, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.centery = 850
        self.key_pressed_flag = True

    def update(self):
        key_pressed = pygame.key.get_pressed()
        #逆時鐘移動
        if key_pressed[pygame.K_RIGHT] and self.key_pressed_flag == True:
            #在Weapon1的位置
            if (self.rect.centerx == 600 and self.rect.centery == 850):
                self.rect.centerx = 900
                self.rect.centery = 750
                self.key_pressed_flag = False
            #在Weapon2的位置
            elif (self.rect.centerx == 900 and self.rect.centery == 750):
                self.rect.centerx = 1000
                self.rect.centery = 450
                self.key_pressed_flag = False
            #在Weapon3的位置
            elif (self.rect.centerx == 1000 and self.rect.centery == 450):
                self.rect.centerx = 900
                self.rect.centery = 150
                self.key_pressed_flag = False
            #在Weapon4的位置
            elif (self.rect.centerx == 900 and self.rect.centery == 150):
                self.rect.centerx = 600
                self.rect.centery = 50
                self.key_pressed_flag = False
            #在Weapon5的位置
            elif (self.rect.centerx == 600 and self.rect.centery == 50):
                self.rect.centerx = 300
                self.rect.centery = 150
                self.key_pressed_flag = False
            #在Weapon6的位置
            elif (self.rect.centerx == 300 and self.rect.centery == 150):
                self.rect.centerx = 200
                self.rect.centery = 450
                self.key_pressed_flag = False
            #在Weapon7的位置
            elif (self.rect.centerx == 200 and self.rect.centery == 450):
                self.rect.centerx = 300
                self.rect.centery = 750
                self.key_pressed_flag = False
            #在Weapon8的位置
            elif (self.rect.centerx == 300 and self.rect.centery == 750):
                self.rect.centerx = 600
                self.rect.centery = 850
                self.key_pressed_flag = False
        #順時鐘移動
        if key_pressed[pygame.K_LEFT] and self.key_pressed_flag == True:
            #在Weapon1的位置
            if (self.rect.centerx == 600 and self.rect.centery == 850):
                self.rect.centerx = 300
                self.rect.centery = 750
                self.key_pressed_flag = False
            #在Weapon8的位置
            elif (self.rect.centerx == 300 and self.rect.centery == 750):
                self.rect.centerx = 200
                self.rect.centery = 450
                self.key_pressed_flag = False
            #在Weapon7的位置
            elif (self.rect.centerx == 200 and self.rect.centery == 450):
                self.rect.centerx = 300
                self.rect.centery = 150
                self.key_pressed_flag = False
            #在Weapon6的位置
            elif (self.rect.centerx == 300 and self.rect.centery == 150):
                self.rect.centerx = 600
                self.rect.centery = 50
                self.key_pressed_flag = False
            #在Weapon5的位置
            elif (self.rect.centerx == 600 and self.rect.centery == 50):
                self.rect.centerx = 900
                self.rect.centery = 150
                self.key_pressed_flag = False
            #在Weapon4的位置
            elif (self.rect.centerx == 900 and self.rect.centery == 150):
                self.rect.centerx = 1000
                self.rect.centery = 450
                self.key_pressed_flag = False
            #在Weapon3的位置
            elif (self.rect.centerx == 1000 and self.rect.centery == 450):
                self.rect.centerx = 900
                self.rect.centery = 750
                self.key_pressed_flag = False
            #在Weapon2的位置
            elif (self.rect.centerx == 900 and self.rect.centery == 750):
                self.rect.centerx = 600
                self.rect.centery = 850
                self.key_pressed_flag = False

    def shoot1(self):
        bullet1 = Bullet1(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet1)
        self.bullets.add(bullet1)
    def shoot2(self):
        bullet2 = Bullet2(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet2)
        self.bullets.add(bullet2)
    def shoot3(self):
        bullet3 = Bullet3(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet3)
        self.bullets.add(bullet3)
    def shoot4(self):
        bullet4 = Bullet4(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet4)
        self.bullets.add(bullet4)
    def shoot5(self):
        bullet5 = Bullet5(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet5)
        self.bullets.add(bullet5)
    def shoot6(self):
        bullet6 = Bullet6(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet6)
        self.bullets.add(bullet6)
    def shoot7(self):
        bullet7 = Bullet7(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet7)
        self.bullets.add(bullet7)
    def shoot8(self):
        bullet8 = Bullet8(self.rect.centerx, self.rect.centery)
        self.all_sprites.add(bullet8)
        self.bullets.add(bullet8)