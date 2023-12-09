import pygame


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


speed = 0.6
speed2 = 0.3
img_x = 90
img_y = 70
img_x1 = random.randint(-1,1)
img_y1 = random.randint(-1,1)
def hero():
    global img_x
    global img_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        img_y -= speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        img_y += speed
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        img_x -= speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        img_x += speed
    screen.blit(img1_s, (img_x, img_y))

def antihero():
    global img_x1
    global img_y1
    keys = pygame.key.get_pressed()

    img_y1 -= speed2
    img_y1 += speed2
    img_x1 -= speed2
    img_x1 += speed2

    screen.blit(img2_s, (img_x1, img_y1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(img_s, (0, 0))

    hero()

    antihero()

    text = font2.render("Start", True, (0,0,225))
    screen.blit(text, (500, 320))
    text = font.render("Welcome", True, (0, 255, 0))
    screen.blit(text, (455, 200))
    text = font2.render("Options", True, (0,0,255))
    screen.blit(text, (480, 350))
    text = font2.render("Exit", True, (255, 0, 0))
    screen.blit(text, (505, 380))

    pygame.display.update()
