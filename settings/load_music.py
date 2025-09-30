import pygame
import os

#載入音樂
shoot_sound = pygame.mixer.Sound(os.path.join("sounds", "shoot.wav"))
shoot_sound.set_volume(0.5)
invade_sound = pygame.mixer.Sound(os.path.join("sounds", "invade.wav"))
invade_sound.set_volume(0.3)
kill_sound = pygame.mixer.Sound(os.path.join("sounds", "kill.wav"))
kill_sound.set_volume(0.5)
heal_sound = pygame.mixer.Sound(os.path.join("sounds", "heal.wav"))
heal_sound.set_volume(0.5)
no_sound = pygame.mixer.Sound(os.path.join("sounds", "no_sound.wav"))
no_sound.set_volume(0.1)
pygame.mixer.music.load(os.path.join("sounds", "bgm.ogg"))
pygame.mixer.music.set_volume(0.7)

#預設音效
Sound1 = shoot_sound
Sound2 = kill_sound
Sound3 = invade_sound
Sound4 = heal_sound