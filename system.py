import pygame as pg
import sys
import webbrowser
from time import sleep as wait
from playsound import playsound
FPS = 60
pg.init()
sc = pg.display.set_mode((800, 600))
pg.display.set_caption('Purpl3 OS on Pygame')
clock = pg.time.Clock()
pg.display.update()

show_menu = False
show_amogus = False
show_themes = False
show_browser = False

theme_r = 255
theme_g = 255
theme_b = 255

font = pg.font.SysFont(None, 30)
text = "Пишите сюда"
input_active = True

os_menu = pg.image.load('os_menu.png')
os_menu_scale = pg.transform.scale(os_menu, (60, 60))
os_menu_scale_rect = os_menu_scale.get_rect(center=(30,575))

wallpaper = pg.image.load('wallpaper.jpg')
wallpaper_scale = pg.transform.scale(wallpaper, (800,600))
wallpaper_scale_rect = wallpaper_scale.get_rect(center=(400,300))

off_button = pg.image.load('off_icon.png')
off_button_scale = pg.transform.scale(off_button, (100,100))
off_button_scale_rect = off_button_scale.get_rect(center=(760,575))

amogus = pg.image.load('amogus.jpg')
amogus_scale = pg.transform.scale(amogus, (250,250))
amogus_scale_rect = amogus_scale.get_rect(center=(450,300))

while True:
    clock.tick(FPS)
    sc.fill((0,0,0))
    sc.blit(wallpaper_scale,wallpaper_scale_rect)
    def print_text(text,x,y,scale,color_r,color_g,color_b):
        f1 = pg.font.Font(None, scale)
        text1 = f1.render(text, True,(color_r, color_g, color_b))
        sc.blit(text1, (x, y))
    print_text('Purpl3 OS',700,10,30,255,255,255)#ватермарк
    
    pg.draw.rect(sc, (theme_r, theme_b,theme_g), (0, 550, 800, 50))#панель
    
    if show_menu==True:
        pg.draw.rect(sc, (theme_r, theme_b,theme_g), (0, 250, 200, 300))#меню
        print_text('Создатель',50,260,30,0,0,0)#ватермарк
        pg.draw.rect(sc, (0,0,0), (0,250,200,40),2)

        print_text('Не нажимать!!!',30,300,30,0,0,0)#ватермарк
        pg.draw.rect(sc, (0,0,0), (0,290,200,40),2)

        print_text('Темы',65,340,30,0,0,0)#ватермарк
        pg.draw.rect(sc, (0,0,0), (0,330,200,40),2)

        print_text('Браузер',50,380,30,0,0,0)#ватермарк
        pg.draw.rect(sc, (0,0,0), (0,370,200,40),2)


    if show_amogus==True:
        show_menu=False
        pg.draw.rect(sc, (255, 255, 255), (300,100,300,400))#база калькулятора
        pg.draw.rect(sc, (255,0,0), (550,100,50,50))
        pg.draw.line(sc,(255,255,255),(550,100),(600,150),3)
        pg.draw.line(sc,(255,255,255),(600,100),(550,150),3)
        sc.blit(amogus_scale,amogus_scale_rect)

    if show_themes==True:
        show_menu=False
        pg.draw.rect(sc, (255, 255, 255), (300,100,300,400))#база калькулятора
        pg.draw.rect(sc, (255,0,0), (550,100,50,50))
        pg.draw.line(sc,(255,255,255),(550,100),(600,150),3)
        pg.draw.line(sc,(255,255,255),(600,100),(550,150),3)
        pg.draw.rect(sc,(0,0,0), (300,100,250,120),2)
        pg.draw.circle(sc,(138,43,226),(410,150),30)    
        print_text('Фиолетовый бриз',325,190,30,0,0,0)#ватермарк

    if show_browser==True:
        show_menu=False
        pg.draw.rect(sc, (255, 255, 255), (300,100,300,400))#база калькулятора
        pg.draw.rect(sc, (255,0,0), (550,100,50,50))
        pg.draw.line(sc,(255,255,255),(550,100),(600,150),3)
        pg.draw.line(sc,(255,255,255),(600,100),(550,150),3)
        pg.draw.rect(sc,(0,0,0),(330,195,230,100),3)
        pg.draw.rect(sc,(0,0,0),(345,300,200,60),3)
        print_text('Поиск',420,320,30,0,0,0)#ватермарк
        text_surf = font.render(text, True, (0, 0, 0))
        sc.blit(text_surf, text_surf.get_rect(center = (450,250)))

    sc.blit(os_menu_scale,os_menu_scale_rect)
    
    sc.blit(off_button_scale,off_button_scale_rect)

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN and input_active:
            if event.key == pg.K_RETURN:
                input_active = False
            elif event.key == pg.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            
            print(pos)
            #--------НАЖАТИЕ НА ПУСК-------
            if pos[0] in range(10,50):
                if pos[1] in range(551,600):#на нажатие пуск
                    show_menu=True
            
            elif pos[0] in range(200,800):
                    show_menu=False
            
            elif pos[1] in range(0,250):
                    show_menu=False
            #--------КНОПКА ВЫКЛЮЧЕНИЯ-------

            if pos[0] in range(740,800):
                if pos[1] in range(551,600):
                    quit()

            #--------ПРИЛОЖЕНИЯ ИЗ МЕНЮ ПУСК-------
            if show_menu==True:
                if pos[0] in range(0,200):#Ссылка на тт создателя
                    if pos[1] in range(250,290):
                        webbrowser.open('https://www.tiktok.com/@purpl3_ai')

            if show_menu==True:
                if pos[0] in range(0,200):#Меню амогуса
                    if pos[1] in range(290,330):
                        show_amogus=True

            if show_amogus==True or show_themes==True or show_browser==True:
                if pos[0] in range(550,600):#В амогусе и темах кнопка закрыть
                    if pos[1] in range(100,150):
                        show_amogus=False
                        show_themes=False
                        show_browser=False
            
            if show_amogus==True:
                if pos[0] in range(325,575):#В амогусе при нажатии амогуса
                    if pos[1] in range(175,425):
                            playsound('./amogus.mp3')

            if show_menu==True:
                if pos[0] in range(0,200):#Меню тем
                    if pos[1] in range(330,370):
                        show_themes=True

            if show_menu==True:
                if pos[0] in range(0,200):#Браузер
                    if pos[1] in range(370,410):
                        show_browser=True

            if show_themes==True:
                if pos[0] in range(300,550):
                    if pos[1] in range(100,220):
                        theme_r = 138
                        theme_b = 43
                        theme_g = 226

            if show_browser==True:
                if pos[0] in range(330,330+230):
                    if pos[1] in range(195,195+100):
                        input_active = True
                        text = ''

            if show_browser==True:
                if pos[0] in range(345,345+200):
                    if pos[1] in range(300,360):
                        input_active = False
                        webbrowser.open(f'https://www.google.com/search?&q={text}')

    pg.display.update()