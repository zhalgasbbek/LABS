import pygame
import sys #sys для системных функций,
from pygame.locals import * #импортирует константы и классы из pygame.
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock() #это объект часов, используемый для контроля частоты кадров.

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coin2 = 0
# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("C:\MyPythonProjects\TSIS\PyGame/files/AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# background sound
pygame.mixer.music.load('C:\MyPythonProjects\TSIS\PyGame/files/background.mp3')
pygame.mixer.music.play(-1) # i use -1 to loop the music

#Enemy, который наследуется от класса pygame.sprite.Sprite. 
# Это означает, что класс Enemy будет иметь все свойства и методы класса pygame.sprite.Sprite, что позволит его использовать вместе с другими спрайтами в группах спрайтов.
# Create a sprite group Enemy
class Enemy(pygame.sprite.Sprite):
    # constructor
    def __init__(self): #Это метод-конструктор класса Enemy, который вызывается при создании нового экземпляра класса Enemy.
        super().__init__() #выполнить инициализацию базовых свойств спрайта.
        self.image = pygame.image.load("C:\MyPythonProjects\TSIS\PyGame/files/Enemy.png")
        self.rect = self.image.get_rect()   # get_rect - возвращает прямоугольник,#: Эта строка создает прямоугольную область (Rect), соответствующую изображению врага.
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    # move method
    def move(self):
        global SCORE #используется для подсчета очков в игре
        self.rect.move_ip(0, SPEED) # перемещает прямоугольную область объекта врага вниз по экрану на расстояние SPEED
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Create a sprite group Player
class Player(pygame.sprite.Sprite): #Создается группа спрайтов для игрока.
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\MyPythonProjects\TSIS\PyGame/files/Player.png")
        self.rect = self.image.get_rect() #определяется его прямоугольная область
        self.rect.center = (160, 520) #начальное положение.
    # move method
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Create a sprite group Coin
class Coin(pygame.sprite.Sprite):
    # constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def move(self):
        global coin2
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()



# Создаются экземпляры классов игрока, врага и монеты.
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups  Группы спрайтов в Pygame позволяют легко управлять несколькими спрайтами одновременно.
# Они предоставляют удобные методы для обновления, отображения и проверки столкновений всех спрайтов в группе.
enemies = pygame.sprite.Group()
enemies.add(E1)
#Это позволяет группе enemies отслеживать и управлять этим конкретным вражеским спрайтом.
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1 #Создается пользовательское событие для увеличения скорости врагов.

pygame.time.set_timer(INC_SPEED, 1000) #Оно будет вызываться каждую секунду (1000 миллисекунд).


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    counter = font_small.render(str(coin2), True, BLACK)
    DISPLAYSURF.blit(counter, (380, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for collision with coins
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        coin2 += 1
        new_coin = Coin() #: Создает новый экземпляр класса монеты.
        coins.add(new_coin) #Добавляет новую монету в группу монет coins.
        all_sprites.add(new_coin) #Добавляет новую монету в группу всех спрайтов all_sprites, чтобы она отображалась на экране.
        new_coin.rect.top = 0
        new_coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:\MyPythonProjects\TSIS\PyGame/files/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
    
    
    