import pygame
from enum import Enum
import sys
#----------display----------
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Т А Н К И   Г Р Я З И   Н Е   Б О Я Т С Я ')
font = pygame.font.SysFont(None, 28)
gameIcon = pygame.image.load('champion.png')
pygame.display.set_icon(gameIcon)
text1 = font.render('W I N', True, (255, 255, 0))
text2 = font.render('B L U E', True, (0, 0, 205))
text3 = font.render('R E D ', True, (225, 0, 0))
#--------trueFALSE-------BOOL
tt1 = True
tt2 = True
#--------------sounds------------
shoot = pygame.mixer.Sound('fire.wav')
fon = pygame.mixer.Sound('background.wav')
collision = pygame.mixer.Sound('collision.wav')
#-----------BULLET---------
class Bullets:
    def __init__(self, x, y, speedx, speedy):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.shot = False
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y),10)
    def move(self):
        if self.shot == True:
            self.x += self.speedx
            self.y += self.speedy
        self.draw()
class Direction(Enum):
    UP = 4
    DOWN = 3
    LEFT = 2
    RIGHT = 1
#-----------TANK------------
class Tank:
    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
        self.x = x
        self.y = y
        self.speed = 1
        self.color = color
        self.width = 40
        self.direction = Direction.UP
        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}
#-----------FIGURE OF TANK---------------
    def draw(self):
        figure = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,(self.x, self.y, self.width, self.width))
#---------Dulo---------
        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, figure, (self.x + self.width + int(self.width / 2), self.y + int(self.width / 2)), 6)
        elif self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, figure, ( self.x - int(self.width / 2), self.y + int(self.width / 2)), 6)
        elif self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, figure, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 6)
        elif self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, figure, (self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)),6)
#--------------selfDIRECTION--------------
    def change_direction(self, direction):
        self.direction = direction
    def move(self):
        if self.direction == Direction.LEFT: self.x -= self.speed
        elif self.direction == Direction.RIGHT: self.x += self.speed
        elif self.direction == Direction.UP:  self.y -= self.speed
        elif self.direction == Direction.DOWN:self.y += self.speed
#-----------THROUGH PALE MAP-----------------
        if(self.x < 0):self.x = 800
        if(self.x > 800): self.x = 0
        if(self.y < 0): self.y = 600
        if(self.y > 600): self.y = 0
        self.draw()
#-------MAIN--------------
heart1 = 3
heart2 = 3
mainloop = True 
red= Tank(300, 300, 1, (225, 0, 0))
blue = Tank(100, 100, 1, (0, 0, 205), pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
tanks = [red, blue ]
bullet1 = Bullets(820, 620, 0, 0)
bullet2 = Bullets(820, 620 , 0,0)
#------FPS
FPS = 120 
clock = pygame.time.Clock ()
fon.play(-1)
while mainloop:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
            if event.key == pygame.K_RETURN and bullet1.shot == False:
                shoot.play()
                bullet1.shot = True
                if red.direction == Direction.LEFT:
                    bullet1.x = red.x - 20
                    bullet1.y = red.y + 20
                    bullet1.speedx = -15
                    bullet1.speedy = 0
                if red.direction == Direction.RIGHT:
                    bullet1.x = red.x + 60
                    bullet1.y = red.y + 20
                    bullet1.speedx = 10
                    bullet1.speedy = 0
                if red.direction == Direction.UP:
                    bullet1.x = red.x + 20
                    bullet1.y = red.y - 20
                    bullet1.speedx = 0
                    bullet1.speedy = -10
                if red.direction == Direction.DOWN:
                    bullet1.x = red.x + 20
                    bullet1.y = red.y + 60
                    bullet1.speedx = 0
                    bullet1.speedy = 10
            if event.key == pygame.K_SPACE and bullet2.shot == False:
                shoot.play()
                bullet2.shot = True
                bullet2.x = blue.x
                bullet2.y = blue.y
                if blue.direction == Direction.LEFT:
                    bullet2.x = blue.x - 20
                    bullet2.y = blue.y + 20
                    bullet2.speedx = -10
                    bullet2.speedy = 0
                if blue.direction == Direction.RIGHT:
                    bullet2.x = blue.x + 60
                    bullet2.y = blue.y + 20
                    bullet2.speedx = 10
                    bullet2.speedy = 0
                if blue.direction == Direction.UP:
                    bullet2.x = blue.x + 20
                    bullet2.y = blue.y - 20
                    bullet2.speedx = 0
                    bullet2.speedy = -10
                if blue.direction == Direction.DOWN:
                    bullet2.x = blue.x + 20
                    bullet2.y = blue.y + 60
                    bullet2.speedx = 0
                    bullet2.speedy = 10
    if bullet1.x < 0 or bullet1.x > 821 or bullet1.y < 0 or bullet1.y > 550:
        bullet1.shot = False
    if bullet2.x < 0 or bullet2.x > 821 or bullet2.y < 0 or bullet2.y > 550:
        bullet2.shot = False
    if bullet1.x in range(blue.x, blue.x + 40) and bullet1.y in range(blue.y, blue.y + 40):
        collision.play()
        bullet1.shot = False
        bullet1.x = 810
        bullet1.y = 610
        heart1 -= 1
        tt1 = True
    if bullet2.x in range(red.x,red.x + 40) and bullet2.y in range(red.y, red.y + 40):
        collision.play()
        bullet2.shot = False
        bullet2.x = 810
        bullet2.y = 610
        heart2 -=1 
        tt2 = True
    if tt1 == True:
        score_1 = font.render("BLUE: " + str(heart1), True, (0, 0, 205))
        tt1 = False
    if tt2 == True:
        score_2 = font.render("RED: " + str(heart2), True, (225, 0, 0))
        tt2 = False
    screen.fill((0, 255,0))
    screen.blit(score_1, (40, 10))
    screen.blit(score_2, (680, 10))
    red.move()
    blue.move()
    bullet1.move()
    bullet2.move()
#------END OF THE GAME------   
    if heart1 <= 0 :
        fon.stop()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
        font = pygame.font.SysFont(None, 64)
        text_3 = font.render('W I N', True, (255, 255, 0))
        text_2 = font.render('R E D', True, (225, 0, 0))
        screen.blit(text_2, (350, 200))
        screen.blit(text_3, (350, 280))
    if heart2 <= 0 :
        fon.stop()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
        font = pygame.font.SysFont('Times new roman', 64)
        text_3 = font.render('W I N', True, (255, 255, 0))
        text_2 = font.render('B L U E', True, (0, 0, 205))
        screen.blit(text_2, (340, 200))
        screen.blit(text_3, (350, 280))        
    pygame.display.flip()  
pygame.quit()
