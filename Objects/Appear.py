import pygame

from Objects.Monster import *
from Objects.Health import *

#出現
class Appear(pygame.sprite.Sprite):
    def __init__(self, all_sprites, appears):
        super().__init__()
        self.all_sprites = all_sprites
        self.appears = appears

    def appear1(self):
        monster1 = Monster1((600, 500), '1')
        self.all_sprites.add(monster1)
        self.appears.add(monster1)
    def appear2(self):
        monster2 = Monster2((600, 500), '2')
        self.all_sprites.add(monster2)
        self.appears.add(monster2)
    def appear3(self):
        monster3 = Monster3((600, 500), '3')
        self.all_sprites.add(monster3)
        self.appears.add(monster3)
    def appear4(self):
        monster4 = Monster4((600, 500), '4')
        self.all_sprites.add(monster4)
        self.appears.add(monster4)
    def appear5(self):
        monster5 = Monster5((600, 500), '5')
        self.all_sprites.add(monster5)
        self.appears.add(monster5)
    def appear6(self):
        monster6 = Monster6((600, 500), '6')
        self.all_sprites.add(monster6)
        self.appears.add(monster6)
    def appear7(self):
        monster7 = Monster7((600, 500), '7')
        self.all_sprites.add(monster7)
        self.appears.add(monster7)
    def appear8(self):
        monster8 = Monster8((600, 500), '8')
        self.all_sprites.add(monster8)
        self.appears.add(monster8)
    def appear9(self):
        health1 = Health1((600, 500))
        self.all_sprites.add(health1)
        self.appears.add(health1)
    def appear10(self):
        health2 = Health2((600, 500))
        self.all_sprites.add(health2)
        self.appears.add(health2)
    def appear11(self):
        health3 = Health3((600, 500))
        self.all_sprites.add(health3)
        self.appears.add(health3)
    def appear12(self):
        health4 = Health4((600, 500))
        self.all_sprites.add(health4)
        self.appears.add(health4)
    def appear13(self):
        health5 = Health5((600, 500))
        self.all_sprites.add(health5)
        self.appears.add(health5)
    def appear14(self):
        health6 = Health6((600, 500))
        self.all_sprites.add(health6)
        self.appears.add(health6)
    def appear15(self):
        health7 = Health7((600, 500))
        self.all_sprites.add(health7)
        self.appears.add(health7)
    def appear16(self):
        health8 = Health8((600, 500))
        self.all_sprites.add(health8)
        self.appears.add(health8)