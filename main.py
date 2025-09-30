import pygame
import random
import os

#設定
from settings.config import *

FPS = 60
Button_clicked = False
Start_clicked = False
Return_clicked = False
Return_S_clicked = False
Again_clicked = False
Time_rate = 1500
Difficulty = 0
Diff_flag = pygame.time.get_ticks()
Rule_flag = False
Rule_page = 1
Setting_flag = False
Market_flag = False
Quit_flag = False
Music_flag = True
Sound_flag = True

#遊戲初始化, 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("星界守衛戰")

#讀取
from settings.load_image import *
from settings.load_music import *
from settings.load_text import *
from settings.btn import *

#物件
from Objects.Appear import *
from Objects.Bullet import *
from Objects.Heal import *
from Objects.Health import *
from Objects.Hole import *
from Objects.Kill import *
from Objects.Life import *
from Objects.Monster import *
from Objects.Player import *
from Objects.Weapon import *

icon = pygame.image.load(os.path.join("images", "icon.png")).convert()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#特殊畫面
def draw_init():
    global Start_clicked, Return_clicked, Button_clicked, Rule_flag, Rule_page, Quit_flag, Setting_flag, Market_flag
    screen.blit(Start_Background_img, (0,0))
    Return_clicked = False
    draw_title(screen, '星界守衛戰', 120, WIDTH/3, HEIGHT/6)
    draw_text(screen, '開始遊戲', 60, WIDTH/14*3, 375)
    draw_text(screen, '規則', 60, WIDTH/6, 500)
    draw_text(screen, '商城', 60, WIDTH/6, 625)
    draw_text(screen, '(尚未開放)', 30, WIDTH/7*2, 640)
    draw_command(screen, '離開', 60, WIDTH/3, 800)
    draw_command(screen, '設定', 60, WIDTH/6, 800)
    pygame.display.update()
    while Button_clicked == False:
        clock.tick(FPS)
        #取得輸入
        for event in pygame.event.get():
            #關閉遊戲
            if event.type == pygame.QUIT:
                pygame.quit()
                Quit_flag = True
                return False
            #點擊事件
            elif event.type == pygame.MOUSEBUTTONUP:
                if btn_Start_rect.collidepoint(event.pos):
                    Start_clicked = True
                    Button_clicked = True
                elif btn_Rule_rect.collidepoint(event.pos):
                    Button_clicked = True
                    Rule_flag = True
                    Rule_page = 1
                elif btn_Setting_rect.collidepoint(event.pos):
                    Button_clicked = True
                    Setting_flag = True
                elif btn_Market_rect.collidepoint(event.pos):
                    Button_clicked = True
                    Market_flag = True
                elif btn_Quit1_rect.collidepoint(event.pos):
                    pygame.quit()
                    Quit_flag = True
                    return False
                
def draw_Rule():
    global Return_clicked, Button_clicked, Rule_flag, Quit_flag, Rule_page
    TOTAL_PAGES = 6
    while Rule_flag:
        Return_clicked = False
        screen.blit(Start_Background_img, (0,0))
        screen.blit(Rule_imgs[Rule_page-1], (295,270))

        # 顯示不同頁
        if Rule_page == 1:
            draw_text(screen, '怪物會跑向八個不同的方向', 50, WIDTH/2, HEIGHT/5)
        elif Rule_page == 2:
            draw_text(screen, '紅色標記是你的位置', 50, WIDTH/2, HEIGHT/8)
            draw_text(screen, '按下空格鍵可以發射當前位置的子彈', 50, WIDTH/2, HEIGHT/5)
        elif Rule_page == 3:
            draw_text(screen, '按左鍵可以往順時鐘方向移動一格', 50, WIDTH/2, HEIGHT/5)
        elif Rule_page == 4:
            draw_text(screen, '按右鍵可以往逆時鐘方向移動一格', 50, WIDTH/2, HEIGHT/5)
        elif Rule_page == 5:
            draw_text(screen, '角落分別有血量和分數', 50, WIDTH/2, HEIGHT/5)
        elif Rule_page == 6:
            draw_text(screen, '遊戲經過一定時間會出現白色怪物', 50, WIDTH/2, HEIGHT/8)
            draw_text(screen, '讓他碰到武器可以回血', 50, WIDTH/2, HEIGHT/5)

        # 畫按鈕
        draw_command(screen, '首頁', 60, WIDTH/2, HEIGHT/8*7)
        if Rule_page > 1:
            draw_command(screen, '上一頁', 60, WIDTH/8, HEIGHT/8*7)
        if Rule_page < TOTAL_PAGES:
            draw_command(screen, '下一頁', 60, WIDTH/8*7, HEIGHT/8*7)
        pygame.display.update()

        while not Return_clicked:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Quit_flag = True
                    return False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if btn_Return_rect.collidepoint(event.pos):
                        Return_clicked = True
                        Rule_flag = False
                        Button_clicked = False
                        Rule_page = 1
                    elif btn_Pre_rect.collidepoint(event.pos) and Rule_page > 1:
                        Return_clicked = True
                        Rule_page -= 1
                    elif btn_Next_rect.collidepoint(event.pos) and Rule_page < TOTAL_PAGES:
                        Return_clicked = True
                        Rule_page += 1

def draw_Setting():
    global Return_S_clicked, Button_clicked, Setting_flag, Quit_flag, Music_flag, Sound_flag, Sound1, Sound2, Sound3, Sound4
    while Setting_flag == True:
        Return_S_clicked = False
        screen.blit(Start_Background_img, (0,0))
        screen.blit(Setting_Background_img, (125,75))
        draw_text(screen, '語言：', 70, WIDTH/4, HEIGHT/2)
        draw_text(screen, '繁體中文', 70, WIDTH/15*7, HEIGHT/2)
        draw_text(screen, '音樂：', 70, WIDTH/4, HEIGHT/7*2)
        draw_text(screen, '音效：', 70, WIDTH/5*3, HEIGHT/7*2)
        draw_command(screen, '返回', 60, WIDTH/2, HEIGHT/6*5)
        if Music_flag == True:
            draw_text(screen, 'ON', 60, 450, HEIGHT/7*2)
        else:
            draw_text(screen, 'OFF', 60, 450, HEIGHT/7*2)
        if Sound_flag == True:
            draw_text(screen, 'ON', 60, 870, HEIGHT/7*2)
        else:
            draw_text(screen, 'OFF', 60, 870, HEIGHT/7*2)
        pygame.display.update()
        while Return_S_clicked == False:
            clock.tick(FPS)

            #取得輸入
            for event in pygame.event.get():
                #關閉遊戲
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Quit_flag = True
                    return False
                #點擊事件
                elif event.type == pygame.MOUSEBUTTONUP:
                    if btn_Return_S_rect.collidepoint(event.pos):
                        Return_S_clicked = True
                        Setting_flag = False
                        Button_clicked = False
                    elif btn_Music_rect.collidepoint(event.pos):
                        if Music_flag == True:
                            Music_flag = False
                            screen.blit(Del_img, (415,260))
                            draw_text(screen, 'OFF', 60, 455, HEIGHT/7*2)
                            pygame.display.update()
                        else:
                            Music_flag = True
                            screen.blit(Del_img, (415,260))
                            draw_text(screen, 'ON', 60, 450, HEIGHT/7*2)
                            pygame.display.update()
                    elif btn_Sound_rect.collidepoint(event.pos):
                        if Sound_flag == True:
                            Sound_flag = False
                            Sound1 = no_sound
                            Sound2 = no_sound
                            Sound3 = no_sound
                            Sound4 = no_sound
                            screen.blit(Del_img, (835,260))
                            draw_text(screen, 'OFF', 60, 875, HEIGHT/7*2)
                            pygame.display.update()
                        else:
                            Sound_flag = True
                            Sound1 = shoot_sound
                            Sound2 = kill_sound
                            Sound3 = invade_sound
                            Sound4 = heal_sound
                            screen.blit(Del_img, (835,260))
                            draw_text(screen, 'ON', 60, 870, HEIGHT/7*2)
                            pygame.display.update()

def draw_Market():
    global Return_S_clicked, Button_clicked, Market_flag, Quit_flag
    while Market_flag == True:
        Return_S_clicked = False
        screen.blit(Start_Background_img, (0,0))
        draw_text(screen, '敬請期待', 100, WIDTH/2, HEIGHT/2)
        draw_text(screen, '返回', 60, WIDTH/2, HEIGHT/6*5)
        pygame.display.update()
        while Return_S_clicked == False:
            clock.tick(FPS)
            #取得輸入
            for event in pygame.event.get():
                #關閉遊戲
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Quit_flag = True
                    return False
                #點擊事件
                elif event.type == pygame.MOUSEBUTTONUP:
                    if btn_Return_S_rect.collidepoint(event.pos):
                        Return_S_clicked = True
                        Market_flag = False
                        Button_clicked = False

def draw_over():
    global Again_clicked, Quit_flag
    screen.blit(Start_Background_img, (0,0))
    draw_text(screen, '遊戲結束', 120, WIDTH/2, HEIGHT/4)
    draw_text(screen, '你的得分：%d' %(Scores), 100, WIDTH/2, HEIGHT/2)
    draw_text(screen, '首頁', 60, WIDTH/4, HEIGHT/4*3)
    draw_text(screen, '離開', 60, WIDTH/4*3, HEIGHT/4*3)
    pygame.display.update()
    while Again_clicked == False:
        clock.tick(FPS)
        #取得輸入
        for event in pygame.event.get():
            #關閉遊戲
            if event.type == pygame.QUIT:
                pygame.quit()
                Quit_flag = True
                return False
            #點擊事件
            elif event.type == pygame.MOUSEBUTTONUP:
                if btn_Again_rect.collidepoint(event.pos):
                    Again_clicked = True
                elif btn_Quit2_rect.collidepoint(event.pos):
                    pygame.quit()
                    Quit_flag = True
                    return False

#遊戲迴圈
show_init = True
running = True
while running == True:
    while show_init == True:
        if Quit_flag == True:
            break
        #初始畫面
        draw_init()

        #開始遊戲
        if Start_clicked == True:
            Last_update = pygame.time.get_ticks()
            Diff_flag = Last_update+1000
            Difficulty = 0
            Appear_flag = Last_update+2000
            show_init = False
            BGM_delay = Last_update+750
            BGM_flag = True
            blood_flag = []
            n = 0
            j = 0

        #規則
        elif Rule_flag == True:
            draw_Rule()
        elif Setting_flag == True:
            draw_Setting()
        elif Market_flag == True:
            draw_Market()

        #分數
        Scores = 0

        #生命
        HP = 3

        #顯示物件
        all_sprites = pygame.sprite.Group()
        appears = pygame.sprite.Group()
        appear = Appear(all_sprites, appears)
        bullets = pygame.sprite.Group()
        weapons = pygame.sprite.Group()
        weapon1 = Weapon1()
        all_sprites.add(weapon1)
        weapons.add(weapon1)
        weapon2 = Weapon2()
        all_sprites.add(weapon2)
        weapons.add(weapon2)
        weapon3 = Weapon3()
        all_sprites.add(weapon3)
        weapons.add(weapon3)
        weapon4 = Weapon4()
        all_sprites.add(weapon4)
        weapons.add(weapon4)
        weapon5 = Weapon5()
        all_sprites.add(weapon5)
        weapons.add(weapon5)
        weapon6 = Weapon6()
        all_sprites.add(weapon6)
        weapons.add(weapon6)
        weapon7 = Weapon7()
        all_sprites.add(weapon7)
        weapons.add(weapon7)
        weapon8 = Weapon8()
        all_sprites.add(weapon8)
        weapons.add(weapon8)
        hole = Hole()
        all_sprites.add(hole)
        life1 = Life1()
        all_sprites.add(life1)
        life2 = Life2()
        all_sprites.add(life2)
        life3 = Life3()
        all_sprites.add(life3)
        player = Player(all_sprites, bullets)
        all_sprites.add(player)

    if Quit_flag == True:
        break

    #限制回傳
    clock.tick(FPS)
    Now = pygame.time.get_ticks()

    #BGM
    if Now > BGM_delay and BGM_flag == True and Music_flag == True:
        BGM_flag = False
        pygame.mixer.music.play(-1)

    #怪物系統
    if Now-Last_update > Time_rate-Difficulty and Now > Appear_flag:
        Last_update = Now
        if Difficulty < 900:
            j = random.randrange(0,8)
            if j == 0:
                appear.appear1()
            elif j == 1:
                appear.appear2()
            elif j == 2:
                appear.appear3()
            elif j == 3:
                appear.appear4()
            elif j == 4:
                appear.appear5()
            elif j == 5:
                appear.appear6()
            elif j == 6:
                appear.appear7()
            elif j == 7:
                appear.appear8()
        else:
            j = random.randrange(0,40)
            if j%8 == 0:
                appear.appear1()
            elif j%8 == 1 and j < 32:
                appear.appear2()
            elif j%8 == 2 and j < 32:
                appear.appear3()
            elif j%8 == 3 and j < 32:
                appear.appear4()
            elif j%8 == 4 and j < 32:
                appear.appear5()
            elif j%8 == 5 and j < 32:
                appear.appear6()
            elif j%8 == 6 and j < 32:
                appear.appear7()
            elif j%8 == 7 and j < 32:
                appear.appear8()
            elif j == 32:
                appear.appear9()
            elif j == 33:
                appear.appear10()
            elif j == 34:
                appear.appear11()
            elif j == 35:
                appear.appear12()
            elif j == 36:
                appear.appear13()
            elif j == 37:
                appear.appear14()
            elif j == 38:
                appear.appear15()
            elif j == 39:
                appear.appear16()
        blood_flag.append(j//8)
        n += 1

    if Now > Diff_flag and Difficulty < 1000:
        Difficulty += 10
        Diff_flag += 500

    #取得輸入
    for event in pygame.event.get():
        #關閉遊戲
        if event.type == pygame.QUIT:
            running = False
        #鍵盤操作
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                player.key_pressed_flag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Sound1.play()
                if player.rect.center == (600, 850):
                    player.shoot1()
                elif player.rect.center == (900, 750):
                    player.shoot2()
                elif player.rect.center == (1000, 450):
                    player.shoot3()
                elif player.rect.center == (900, 150):
                    player.shoot4()
                elif player.rect.center == (600, 50):
                    player.shoot5()
                elif player.rect.center == (300, 150):
                    player.shoot6()
                elif player.rect.center == (200, 450):
                    player.shoot7()
                elif player.rect.center == (300, 750):
                    player.shoot8()

    #更新遊戲
    all_sprites.update()

    #子彈打到怪物
    Hits = pygame.sprite.groupcollide(appears, bullets, True, True, pygame.sprite.collide_circle)
    for Hit in Hits:
        Scores += Hit.radius*5
        kill = Kill(Hit.rect.center)
        all_sprites.add(kill)
        Sound2.play()

    #碰到武器
    Invades = pygame.sprite.groupcollide(appears, weapons, True, False, pygame.sprite.collide_circle)
    for Invade in Invades:
        #一般怪物碰到武器
        if blood_flag[n-3] < 4:
            HP -= 1
            kill = Kill(Invade.rect.center)
            all_sprites.add(kill)
            Sound3.play()
            if HP == 2:
                all_sprites.remove(life3)
            elif HP == 1:
                all_sprites.remove(life2)
       
        #補血怪碰到武器
        elif blood_flag[n-3] == 4:
            heal = Heal(Invade.rect.center)
            all_sprites.add(heal)
            Sound4.play()
            if HP == 1:
                all_sprites.add(life2)
                HP += 1
            elif HP == 2:
                all_sprites.add(life3)
                HP += 1

    #畫面顯示
    screen.blit(Background_img, (0,0))
    all_sprites.draw(screen)
    draw_text(screen, str(Scores), 70, WIDTH-50, 50)
   
    #生命值歸零
    if HP == 0:
        #判定重製
        pygame.mixer.music.stop()
        show_init = True
        Button_clicked = False
        Start_clicked = False
        Again_clicked = False

        #結束畫面
        draw_over()

    if Quit_flag == True:
        break
    pygame.display.update()

pygame.quit()