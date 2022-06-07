#Spaceinvaders with pygame

import pygame
from sys import exit
import random

class Ship:
    def __init__(self,surf,x,y):
        self.health = 100
        self.ammo=0
        self.surf=surf
        self.x=x
        self.y=y

    def show(self):
        self.surf.blit(self.img,(self.x,self.y))

    def collision(self,obj):
        return collide(self,obj)

class Player(Ship):
    def __init__(self,surf,x,y):
        super().__init__(surf,x,y)
        self.img=pygame.image.load("player.png")
        self.mask=pygame.mask.from_surface(self.img)
        self.lv=1
        self.xp=0
        self.ammo=30


class Enemy(Ship):
    def __init__(self,surf,x,y):
        super().__init__(surf,x,y)
        self.img=pygame.image.load("enemy.png")
        self.mask=pygame.mask.from_surface(self.img)


    def move(self):
        self.y+=1

class Bullet:
    def __init__(self,surf,x,y):
        self.surf=surf
        self.x=x
        self.y=y

    def show(self):
        self.surf.blit(self.img,(self.x,self.y))

    def move(self,lv):
        self.y-=1.5*(lv/2)

class playerBullet(Bullet):
    def __init__(self,surf,x,y):
        super().__init__(surf,x,y)
        self.img=pygame.image.load("bullet.png")
        self.mask=pygame.mask.from_surface(self.img)

class enemyBullet(Bullet):
    def __init__(self,surf,x,y):
        super().__init__(surf,x,y)
        self.img=pygame.image.load("ebullet.png")
        self.mask=pygame.mask.from_surface(self.img)

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

    p=Player(screen,(width/2)-25,400)

    font = pygame.font.Font("freesansbold.ttf",18)

    bullets=[]
    enemies=[]

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if p.ammo > 0:
                        bullet = playerBullet(screen,p.x+25,p.y)
                        bullets.append(bullet)
                        p.ammo-=1

        screen.fill("black")

        text_lv = font.render(f"Level: {p.lv}",1,"white")
        text_hp = font.render(f"Health: {p.health}",1,"white")
        text_ammo = font.render(f"Ammo: {p.ammo}",1,"white")
        screen.blit(text_hp,(1,1))
        screen.blit(text_lv,(width-text_lv.get_rect().width,1))
        screen.blit(text_ammo,(1,text_hp.get_rect().height+1))
        
        p.show()

        if not enemies:
            i=0
            while i<p.lv:
                enemies.append(Enemy(screen,random.randint(0,width-50),random.randint(-200,-50)))
                i+=1

        for bullet in bullets:
            bullet.move(p.lv)
            bullet.show()
            if bullet.y<0:
                bullets.remove(bullet)
            for e in enemies:
                if e.collision(bullet):
                    bullets.remove(bullet)
                    e.health-=20

        for e in enemies:
            if e.health > 0:
                e.move()
                e.show()
            else:
                enemies.remove(e)
                p.xp+=10/p.lv
                p.ammo+=5
                if p.xp >=100 and p.lv!=20:
                    p.lv+=1
                    p.xp=p.xp-100
                    p.ammo+=10
                    p.health+=10
                    if p.health>100:
                        p.health=100
            if p.collision(e):
                p.health-=5
                p.ammo+=2
                enemies.remove(e)
            if e.y > height:
                enemies.remove(e)
                p.health-=2

        if p.health <= 0:
            pygame.quit()
            exit()


        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] == True and p.y>0:
            p.y -= 3
        if keys[pygame.K_s] == True and p.y+50<height:
            p.y += 3
        if keys[pygame.K_a] == True and p.x>0:
            p.x -= 3
        if keys[pygame.K_d] == True and p.x+50<width:
            p.x += 3

        pygame.display.update()
        pygame.time.delay(10)


main()