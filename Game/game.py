import pygame
import random


pygame.init()

screen_width = 1080
screen_hight = 720

screen = pygame.display.set_mode((screen_width, screen_hight))

font = pygame.font.SysFont("Goudy Stout обычный", 50)
font2 = pygame.font.SysFont("TimesNewRoman", 30)
img = pygame.image.load("img/menu.jpg")
img_s = pygame.transform.scale(img, (1080, 720))
img1 = pygame.image.load("img/zmeya.png")
img1_s = pygame.transform.scale(img1, (100, 100))
img2 = pygame.image.load("img/demon.png")
img2_s = pygame.transform.scale(img2, (100, 100))
sound_stop = pygame.mixer.Sound("Sounds/vzryiv-yadernoy-bombyi.mp3")
sound_antihero = pygame.mixer.Sound("Sounds/zombi-boretsya-s-chelovekom-leja-na-zemle-30059.mp3")
sound_hero = pygame.mixer.Sound("Sounds/Звук Шаги по железной лестнице, ботинки, вверх и вниз.mp3")

speed = 0.6
speed2 = 0.5
img_x = 90
img_y = 70
img_x1 = random.randint(800,980)
img_y1 = random.randint(0,620)
koordinate = random.randint(0,3)


def hero():
    global img_x
    global img_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        img_y -= speed
        sound_hero.play()
    elif keys[pygame.K_s]:
        img_y += speed
        sound_hero.play()
    elif keys[pygame.K_a]:
        img_x -= speed
        sound_hero.play()
    elif keys[pygame.K_d]:
        img_x += speed
        sound_hero.play()
    else:
        sound_hero.stop()
    screen.blit(img1_s, (img_x, img_y))

def antihero():
    global img_x1
    global img_y1
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        img_y1 -= speed2
        sound_antihero.play()
    elif keys[pygame.K_DOWN]:
        img_y1 += speed2
        sound_antihero.play()
    elif keys[pygame.K_LEFT]:
        img_x1 -= speed2
        sound_antihero.play()
    elif keys[pygame.K_RIGHT]:
        img_x1 += speed2
        sound_antihero.play()
    else:
        sound_antihero.stop()
    screen.blit(img2_s, (img_x1, img_y1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(img_s, (0, 0))

    hero()
    antihero()
    if img_x + 100  > img_x1 and img_x < img_x1 + 100 and img_y + 100 > img_y1 and img_y < img_y1 + 100:
        speed = 0
        speed2 = 0
        sound_stop.play()
    else:
        pass
    text = font2.render("Start", True, (0,0,225))
    screen.blit(text, (500, 320))
    text = font.render("Welcome", True, (0, 255, 0))
    screen.blit(text, (455, 200))
    text = font2.render("Options", True, (0,0,255))
    screen.blit(text, (480, 350))
    text = font2.render("Exit", True, (255, 0, 0))
    screen.blit(text, (505, 380))

    pygame.display.update()
