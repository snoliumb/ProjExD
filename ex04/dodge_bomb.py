import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
def crash():
    tkm.showerror("Game Over")

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))#スクリーン
    screen_rct = screen_sfc.get_rect()
    being_sfc = pg.image.load("fig/pg_bg.jpg")#
    being_rct = being_sfc.get_rect()
    screen_sfc.blit(being_sfc, being_rct)

    kkimg_sfc = pg.image.load("fig/6.png")#自機（こうかとん）
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    image = pg.Surface((20,20))#敵弾
    image.set_colorkey(0, 0)
    pg.draw.circle(image, (255, 0, 0), (10,10), 10)
    bomb_rct = image.get_rect()
    a = random.randint(300, 1300)
    b = random.randint(300, 600)
    bomb_rct.center = a, b
    vx, vy = 1, 1

    en = pg.Surface((100,100))#障害物（当たったらゲームオーバー）
    image.set_colorkey(0, 0)
    bomb2_rct = en.get_rect()
    c = random.randint(300, 1300)
    d = random.randint(300, 600)
    bomb2_rct.center = c, d

    while True:
        screen_sfc.blit(being_sfc, being_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        bomb_rct.move_ip(vx, vy)
        screen_sfc.blit(image, bomb_rct)
        screen_sfc.blit(en, bomb2_rct)#表示の処理

        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if pg.key.get_pressed()[pg.K_UP]:#自機の移の動処理
             kkimg_rct.move_ip(0, -1)
        if pg.key.get_pressed()[pg.K_DOWN]:
            kkimg_rct.move_ip(0, 1)
        if pg.key.get_pressed()[pg.K_LEFT]:
            kkimg_rct.move_ip(-1, 0)
        if pg.key.get_pressed()[pg.K_RIGHT]:
             kkimg_rct.move_ip(1, 0)

        if check_bound(kkimg_rct, screen_rct) != (1, 1):#自機が画面端にいる時の処理
            if pg.key.get_pressed()[pg.K_UP]:
                 kkimg_rct.move_ip(0, 1)
            if pg.key.get_pressed()[pg.K_DOWN]:
                kkimg_rct.move_ip(0, -1)
            if pg.key.get_pressed()[pg.K_LEFT]:
                kkimg_rct.move_ip(1, 0)
            if pg.key.get_pressed()[pg.K_RIGHT]:
                kkimg_rct.move_ip(-1, 0)
        
        yoko, tate = check_bound(bomb_rct,screen_rct)#敵弾の反射の処理
        vx *= yoko
        vy *= tate

        if kkimg_rct.colliderect(bomb_rct):#敵弾に当たったとき
            crash()
            return
        if kkimg_rct.colliderect(bomb2_rct):#障害物に当たったとき
            crash()
            return


            
        pg.display.update()
        clock.tick(1000)
    
def check_bound(rct, scr_rct):#反射の実際の処理
    yoko, tate = +1, +1

    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1  

    if rct.top < scr_rct.top   or scr_rct.bottom < rct.bottom : tate = -1
    return yoko, tate
    

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
    