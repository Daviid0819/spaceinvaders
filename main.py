#Spaceinvaders with pygame

# weapon upgrade
# 1. thing -> weapon lv text
# 2. thing -> weapon bullet sizes and bullet speed
# 3. thing -> weapon upgrade when enemy killed

import pygame
from sys import exit

class Ship:
    def __init__(self,surf,x,y):
        self.health = 100
        self.surf=surf
        self.x=x
        self.y=y

    def show(self,screen):
        screen.blit(self.img,(self.x,self.y))

class Player(Ship):
    def __init__(self,surf,x,y):
        super().__init__(surf,x,y)
        self.img=pygame.image.load("player.png")
        self.mask=pygame.mask.from_surface(self.img)


class Enemy(Ship):
    def __init__(self,surf,x,y):
        super().__init__(surf,x,y)
        self.img=pygame.image.load("enemy.png")
        self.mask=pygame.mask.from_surface(self.img)


    def move(self):
        self.y+=1

class playerBullet:
    def __init__(self,surf,x,y):
        self.surf=surf
        self.x=x
        self.y=y
        self.img=pygame.image.load("bullet.png")
        self.mask=pygame.mask.from_surface(self.img)

    def show(self,screen):
        screen.blit(self.img,(self.x,self.y))

    def move(self):
        self.y-=2

    def collision(self,obj):
        return collide(self,obj)

def collide(obj1,obj2):
    offset_x=obj2.x-obj1.x
    offset_y=obj2.y-obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None


def main():
    pygame.init()
    width=500
    height=700
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("GTA VI")
    clock = pygame.time.Clock()
    FPS=60

    p=Player(screen,0,350)

    velocity=3

    bullets=[]
    e=Enemy(screen,300,-100)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = playerBullet(screen,p.x+25,p.y)
                    bullets.append(bullet)

        screen.fill("black")
        
        p.show(screen)

        for bullet in bullets:
            bullet.move()
            bullet.show(screen)
            if bullet.collision(e):
                bullets.remove(bullet)
                e.health-=12
                print(e.health)

        if e.health > 0:
            e.move()
            e.show(screen)


        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] == True and p.y>0:
            p.y -= velocity
        if keys[pygame.K_s] == True and p.y+50<height:
            p.y += velocity
        if keys[pygame.K_a] == True and p.x>0:
            p.x -= velocity
        if keys[pygame.K_d] == True and p.x+50<width:
            p.x += velocity

        #if p.img.get_rect().colliderect(e.img.get_rect()):
           # pygame.draw.rect(screen,"red",p.img.get_rect(),4)


        pygame.display.update()
        pygame.time.delay(10)


main()