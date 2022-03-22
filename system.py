import pygame as pg
import sys
import webbrowser
from time import sleep as wait
from playsound import playsound
import configparser
import configparser
config = configparser.ConfigParser()

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
show_easter_egg = False

config.read('settings.ini')
if str(config.get('DEFAULT', 'theme'))=='white':#если в файле settings.ini переменная theme есть white то сделать белую тему
    theme_r = 255
    theme_g = 255
    theme_b = 255
elif str(config.get('DEFAULT', 'theme'))=='purple':#то что также но с фиолетовой темой
    theme_r = 138
    theme_b = 43
    theme_g = 226

font = pg.font.SysFont(None, 30)
text = "Пишите сюда"
input_active = True

print(str(config.get('DEFAULT', 'theme')))

#--------------Функции-----------
def image(source_image,transform_x,transform_y,pos_x,pos_y):
    picture = pg.image.load(source_image)
    picture_scale = pg.transform.scale(picture, (transform_x,transform_y))
    picture_scale_rect = picture_scale.get_rect(center=(pos_x,pos_y))
    sc.blit(picture_scale,picture_scale_rect)


def base():
    pg.draw.rect(sc, (255, 255, 255), (300,100,300,400))#база для приложений
    pg.draw.rect(sc, (255,0,0), (550,100,50,50))
    pg.draw.line(sc,(255,255,255),(550,100),(600,150),3)
    pg.draw.line(sc,(255,255,255),(600,100),(550,150),3)

def print_text(text,x,y,scale,color_r,color_g,color_b):
        f1 = pg.font.Font(None, scale)
        text1 = f1.render(text, True,(color_r, color_g, color_b))
        sc.blit(text1, (x, y))
while True:
    clock.tick(FPS)
    sc.fill((0,0,0))
    image('wallpaper.jpg',800,600,400,300)
    
    print_text('Purpl3 OS',700,10,30,255,255,255)#пасхалка
    
    pg.draw.rect(sc, (theme_r, theme_b,theme_g), (0, 550, 800, 50))#панель
    
    if show_menu==True:
        pg.draw.rect(sc, (theme_r, theme_b,theme_g), (0, 250, 200, 300))#меню приложений
        print_text('Создатель',50,260,30,0,0,0)#октрывает ссыллку в браузере на тик ток создателя
        pg.draw.rect(sc, (0,0,0), (0,250,200,40),2)

        print_text('Не нажимать!!!',30,300,30,0,0,0)#пасхалка
        pg.draw.rect(sc, (0,0,0), (0,290,200,40),2)

        print_text('Темы',65,340,30,0,0,0)#октрывает меню тем
        pg.draw.rect(sc, (0,0,0), (0,330,200,40),2)

        print_text('Браузер',50,380,30,0,0,0)#октрывает меню браузера
        pg.draw.rect(sc, (0,0,0), (0,370,200,40),2)


    if show_amogus==True:
        show_menu=False
        base()
        image('amogus.jpg',250,250,450,300)
        #sc.blit(amogus_scale,amogus_scale_rect)

    if show_themes==True:
        show_menu=False
        base()
        pg.draw.rect(sc,(0,0,0), (300,100,250,120),2)
        pg.draw.circle(sc,(138,43,226),(410,150),30)    
        print_text('Purple',380,190,30,0,0,0)#выбор темы

        pg.draw.rect(sc,(0,0,0), (300,220,250,120),2)
        pg.draw.circle(sc,(0,0,0),(410,270),30) 
        print_text('Обычная тема',340,310,30,0,0,0)#выбор темы

    if show_browser==True:
        show_menu=False
        base()
        pg.draw.rect(sc,(0,0,0),(330,195,230,100),3)
        pg.draw.rect(sc,(0,0,0),(345,300,200,60),3)
        print_text('Поиск',420,320,30,0,0,0)#кнопка поиска в браузере
        text_surf = font.render(text, True, (0, 0, 0))
        sc.blit(text_surf, text_surf.get_rect(center = (450,250)))

    if show_easter_egg==True:#Если нажать на пасхалку 
        show_menu=False
        base()
        print_text('Purpl3 OS Версии 2022 года\n',300,320,30,0,0,0)#пасхалка


    image('os_menu.png',60,60,30,575)
    image('off_icon.png',100,100,760,575)
    
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

            if show_amogus==True or show_themes==True or show_browser==True or show_easter_egg==True:
                if pos[0] in range(550,600):#В амогусе и темах кнопка закрыть
                    if pos[1] in range(100,150):
                        show_amogus=False
                        show_themes=False
                        show_browser=False
                        show_easter_egg=False
            
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

            if show_themes==True:#Меняет тему на фиолетавою
                if pos[0] in range(300,550):
                    if pos[1] in range(100,220):
                        config['DEFAULT'] = {'theme': 'purple'}
                        with open('settings.ini', 'w') as configfile:config.write(configfile)
                        theme_r = 138
                        theme_b = 43
                        theme_g = 226

                if pos[0] in range(300,550):
                    if pos[1] in range(220,220+120):
                        config['DEFAULT'] = {'theme': 'white'}
                        with open('settings.ini', 'w') as configfile:config.write(configfile)
                        theme_r = 255
                        theme_b = 255
                        theme_g = 255


            if show_browser==True:#Браузер строка поиска
                if pos[0] in range(330,330+230):
                    if pos[1] in range(195,195+100):
                        input_active = True
                        text = ''

            if show_browser==True:#Браузер кнопка поиск
                if pos[0] in range(345,345+200):
                    if pos[1] in range(300,360):
                        input_active = False
                        webbrowser.open(f'https://www.google.com/search?&q={text}')

            if show_menu==False and show_amogus==False and show_themes==False and show_browser==False:
                if pos[0] in range(695,800):
                    if pos[1] in range(2,33):
                        show_easter_egg=True


    pg.display.update()