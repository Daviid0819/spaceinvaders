#Spaceinvaders with pygame

import pygame
from sys import exit

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

class Enemy:
    def __init__(self,surf,x,y):
        self.surf=surf
        self.x=x
        self.y=y
        self.img=pygame.image.load("enemy.png")
        self.mask=pygame.mask.from_surface(self.img)

    def show(self,screen):
        screen.blit(self.img,(self.x,self.y))

    def move(self):
        self.y+=1

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

    player = pygame.image.load("player.png")
    p_rect = player.get_rect()
    p_rect.x = 0
    p_rect.y = 350
    health=100

    velocity=3

    bullets=[]
    e=Enemy(screen,300,-100)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill("black")
        screen.blit(player,p_rect)

        e.move()
        e.show(screen)

        for bullet in bullets:
            bullet.move()
            bullet.show(screen)
            if bullet.collision(e):
                pygame.draw.rect(screen, "blue", pygame.Rect(bullet.x,bullet.y,10,20), 10)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] == True and p_rect.y>0:
            p_rect.y -= velocity
        if keys[pygame.K_s] == True and p_rect.y+50<height:
            p_rect.y += velocity
        if keys[pygame.K_a] == True and p_rect.x>0:
            p_rect.x -= velocity
        if keys[pygame.K_d] == True and p_rect.x+50<width:
            p_rect.x += velocity
        if keys[pygame.K_SPACE] == True:
            bullet = playerBullet(screen,p_rect.x+25,p_rect.y)
            bullets.append(bullet)

        if p_rect.colliderect(e.img.get_rect()):
            pygame.draw.rect(screen,"red",p_rect,4)


        pygame.display.update()
        pygame.time.delay(10)


main()