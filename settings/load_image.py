import pygame
import os

from settings.config import *

Background_img = pygame.image.load(os.path.join("images", "Background.png")).convert()
Setting_Background_img = pygame.image.load(os.path.join("images", "Setting_Background.png")).convert()
Setting_Background_img.set_colorkey(BLACK)
Start_Background_img = pygame.image.load(os.path.join("images", "Start_Background.png")).convert()
Del_img = pygame.image.load(os.path.join("images", "Del.png")).convert()
Del_img.set_colorkey(BLACK)
Rule_imgs = []
for i in range(1,7):
    Rule_img = (pygame.image.load(os.path.join("images", f"Rule{i}.png")).convert())
    Rule_img.set_colorkey(BLACK)
    Rule_imgs.append(pygame.transform.scale(Rule_img, (600, 500)))
Life_img = pygame.image.load(os.path.join("images", "Life.png")).convert()
Mark_img = pygame.image.load(os.path.join("images", "Mark.png")).convert()
Bullet15_img = pygame.image.load(os.path.join("images", "Bullet1,5.png")).convert()
Bullet26_img = pygame.image.load(os.path.join("images", "Bullet2,6.png")).convert()
Bullet37_img = pygame.image.load(os.path.join("images", "Bullet3,7.png")).convert()
Bullet48_img = pygame.image.load(os.path.join("images", "Bullet4,8.png")).convert()
Kill_anim = []
for i in range(1,6):
    Kill_img = pygame.image.load(os.path.join("images", f"kill{i}.png")).convert()
    Kill_img.set_colorkey(BLACK)
    Kill_anim.append(pygame.transform.scale(Kill_img, (150, 150)))
Heal_anim = []
for i in range(1,6):
    Heal_img = pygame.image.load(os.path.join("images", f"heal{i}.png")).convert()
    Heal_img.set_colorkey(BLACK)
    Heal_anim.append(pygame.transform.scale(Heal_img, (150, 150)))
Weapon_img = []
for i in range(1,9):
    Weapon_img.append(pygame.image.load(os.path.join("images", f"Weapon{i}.png")).convert())
Hole_anim = []
for i in range(1,9):
    Hole_img = pygame.image.load(os.path.join("images", f"Hole{i}.png")).convert()
    Hole_img.set_colorkey(BLACK)
    Hole_anim.append(pygame.transform.scale(Hole_img, (150, 150)))
Monster_anim = {}
Monster_anim['1'] = []
Monster_anim['2'] = []
Monster_anim['3'] = []
Monster_anim['4'] = []
Monster_anim['5'] = []
Monster_anim['6'] = []
Monster_anim['7'] = []
Monster_anim['8'] = []
for i in range(1,5):
    Monster1_img = pygame.image.load(os.path.join("images", f"Monster1-{i}.png")).convert()
    Monster1_img.set_colorkey(BLACK)
    Monster_anim['1'].append(pygame.transform.scale(Monster1_img, (150, 150)))
for i in range(1,5):
    Monster2_img = pygame.image.load(os.path.join("images", f"Monster2-{i}.png")).convert()
    Monster2_img.set_colorkey(BLACK)
    Monster_anim['2'].append(pygame.transform.scale(Monster2_img, (150, 150)))
for i in range(1,5):
    Monster3_img = pygame.image.load(os.path.join("images", f"Monster3-{i}.png")).convert()
    Monster3_img.set_colorkey(BLACK)
    Monster_anim['3'].append(pygame.transform.scale(Monster3_img, (150, 150)))
for i in range(1,5):
    Monster4_img = pygame.image.load(os.path.join("images", f"Monster4-{i}.png")).convert()
    Monster4_img.set_colorkey(BLACK)
    Monster_anim['4'].append(pygame.transform.scale(Monster4_img, (150, 150)))
for i in range(1,5):
    Monster5_img = pygame.image.load(os.path.join("images", f"Monster5-{i}.png")).convert()
    Monster5_img.set_colorkey(BLACK)
    Monster_anim['5'].append(pygame.transform.scale(Monster5_img, (150, 150)))
for i in range(1,5):
    Monster6_img = pygame.image.load(os.path.join("images", f"Monster6-{i}.png")).convert()
    Monster6_img.set_colorkey(BLACK)
    Monster_anim['6'].append(pygame.transform.scale(Monster6_img, (150, 150)))
for i in range(1,5):
    Monster7_img = pygame.image.load(os.path.join("images", f"Monster7-{i}.png")).convert()
    Monster7_img.set_colorkey(BLACK)
    Monster_anim['7'].append(pygame.transform.scale(Monster7_img, (150, 150)))
for i in range(1,5):
    Monster8_img = pygame.image.load(os.path.join("images", f"Monster8-{i}.png")).convert()
    Monster8_img.set_colorkey(BLACK)
    Monster_anim['8'].append(pygame.transform.scale(Monster8_img, (150, 150)))
Health_img = []
for i in range(1,9):
    Health_img.append(pygame.image.load(os.path.join("images", f"Health{i}.png")).convert())