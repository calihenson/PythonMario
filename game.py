# Name: Caroline Henson
# Data: December 8, 2022
# Assignment: #8

import pygame
import time

from pygame.locals import*
from time import sleep

class Sprite():
    def __init__(self, xPos, yPos, width, height):
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height

class Mario(Sprite):
    def __init__(self):
        super().__init__(0, 0, 60, 95)
        self.imageM = []
        self.imageNow = 0
        for i in range(5):
            self.imageM.append(pygame.image.load("mario{}.png".format(i)))
        self.numFrames = 0
        self.pipeOrGround = True
        self.px = self.x
        self.py = self.y

    def getOutOfPipe(self, p):
        if((self.x + self.w < p.x + p.w) and (self.px + self.w <= p.x)):
            # print("mario: pipe left side collision");
            self.x = p.x - self.w;

        if((self.x > p.x) and (self.px >= p.x + p.w)):
            # print("mario: pipe right side collision")
            self.x = p.x + p.w

        if((self.y + self.h < p.y + p.h) and (self.py + self.h <= p.y)):
            # print("mario: pipe top collision")
            self.y = p.y - self.h
            self.pipeOrGround = True

        if((self.y > p.y) and (self.py >= p.y + p.h)):
            # print("mario: pipe bottom collision")
            self.y = p.y + p.h

    def jump(self):
        self.jumpVelocity = -30

        if(self.numFrames < 10):
            self.pipeOrGround = False
            self.y += self.jumpVelocity

    def walk(self):
        self.imageNow = self.imageNow + 1
        if(self.imageNow > 4):
            self.imageNow = 0

    def setPreviousPosition(self):
        self.px = self.x
        self.py = self.y

    def update(self):
        self.gravity = 9
        self.vertVelocity = 0
        self.vertVelocity += self.gravity

        self.numFrames += 1

        self.y += self.vertVelocity

        if((self.y > 550 - self.h) or (self.pipeOrGround == True)):
            # self.vertVelocity = 0
            self.numFrames = 0
            self.pipeOrGround = True
            self.y = 550 - self.h

    def isMario(self):
        return True

    def isPipe(self):
        return False

    def isGoomba(self):
        return False

    def isChaos(self):
        return False

    def isFireball(self):
        return False

    def isCollisionL(self):
        return False

    def isCollisionR(self):
        return False

    def draw(self, screen, scrollPosX):
        screen.blit(self.imageM[self.imageNow], (self.x - scrollPosX, self.y, self.w, self.h))

class Pipe(Sprite):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos, 55, 400)
        self.image = pygame.image.load("pipe.png")

    def update(self):
        pass

    def isMario(self):
        return False

    def isPipe(self):
        return True

    def isGoomba(self):
        return False

    def isChaos(self):
        return False

    def isFireball(self):
        return False

    def isCollisionL(self):
        return False

    def isCollisionR(self):
        return False

    def draw(self, screen, scrollPos):
        screen.blit(self.image, (self.x - scrollPos, self.y, self.w, self.h))

class Goomba(Sprite):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos, 37, 45)
        self.image = pygame.image.load("goomba.png")
        self.px = self.x
        self.py = self.y
        self.goombaF = False
        self.collisionL = False
        self.collisionR = False

    def getOutOfPipeG(self, p):
        if((self.x + self.w < p.x + p.w) and (self.px + self.w <= p.x)):
            # print("goomba: pipe left side collision")
            self.x = p.x - self.w
            self.collisionL = True
            self.collisionR = False

        if((self.x > p.x) and (self.px >= p.x + p.w)):
            # print("goomba: pipe right side collision")
            self.x = p.x + p.w
            self.collisionL = False
            self.collisionR = True

    def setPreviousPosition(self):
        self.px = self.x
        self.py = self.y

    def update(self):
        self.start = True

        if(self.start == True):
            self.x += 4

    def isMario(self):
        return False

    def isPipe(self):
        return False

    def isGoomba(self):
        return True

    def isChaos(self):
        return False

    def isFireball(self):
        return False

    def isCollisionL(self):
        if(self.collisionL == True):
            return True
        else:
            return False

    def isCollisionR(self):
        if(self.collisionR == True):
            return True
        else:
            return False

    def draw(self, screen, scrollPos):
        screen.blit(self.image, (self.x - scrollPos, self.y, self.w, self.h))

class FireGoomba(Sprite):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos, 37, 45)
        self.image = pygame.image.load("goomba_fire.png")

    def update(self):
        pass

    def isMario(self):
        return False

    def isPipe(self):
        return False

    def isGoomba(self):
        return False

    def isChaos(self):
        return True

    def isFireball(self):
        return False

    def isCollisionL(self):
        return False

    def isCollisionR(self):
        return False

    def draw(self, screen, scrollPos):
        screen.blit(self.image, (self.x - scrollPos, self.y, self.w, self.h))

class Fireball(Sprite):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos, 47, 47)
        self.image = pygame.image.load("fireball.png")
        self.vertVelocity = 0

    def update(self):
        self.x += 10

        self.vertVelocity += 5
        self.y += self.vertVelocity

        if(self.y > 505):
            self.y = 505

            if(self.y == 505):
                self.vertVelocity += -60

    def isMario(self):
        return False

    def isPipe(self):
        return False

    def isGoomba(self):
        return False

    def isChaos(self):
        return False

    def isFireball(self):
        return True

    def isCollisionL(self):
        return False

    def isCollisionR(self):
        return False

    def draw(self, screen, scrollPos):
        screen.blit(self.image, (self.x - scrollPos, self.y, self.w, self.h))

class Model():
    def __init__(self):
        self.mario = Mario()
        self.sprites = []
        self.sprites.append(self.mario)
        self.sprites.append(Pipe(120, 450))
        self.sprites.append(Pipe(430, 370))
        self.sprites.append(Pipe(600, 450))
        self.sprites.append(Pipe(800, 380))
        self.sprites.append(Pipe(1000, 470))
        self.sprites.append(Pipe(1225, 420))
        self.sprites.append(Pipe(1300, 310))
        self.sprites.append(Goomba(300, 505))
        self.sprites.append(Goomba(500, 505))
        self.sprites.append(Goomba(900, 505))
        self.sprites.append(Goomba(950, 505))
        self.sprites.append(Goomba(1100, 505))
        self.fireFrames = 0

    def isThereACollision(self, a, b):
        # if he is not colliding
        if(a.x + a.w < b.x):
            return False
        if(a.x > b.x + b.w):
            return False
        if(a.y + a.h < b.y):
            return False
        if(a.y > b.y + b.h):
            return False

        # if he is not NOT colliding
        else:
            return True

    def addChaos(self, x, y):
        self.sprites.append(FireGoomba(x, y))

    def addFireball(self):
        self.sprites.append(Fireball(self.mario.x, self.mario.y))

    def update(self):
        for sprite in self.sprites:
            sprite.update()
        
            if(sprite.isMario()):
                for i in self.sprites:
                    if(i.isPipe()):
                        self.checkM = self.isThereACollision(sprite, i)

                        if(self.checkM == True):
                            # print("mario v pipe: collision detected")
                            self.mario.getOutOfPipe(i)

            if(sprite.isGoomba()):
                for j in self.sprites:
                    if(j.isPipe()):
                        self.checkG = self.isThereACollision(sprite, j)

                        if(self.checkG == True):
                            # print("goomba v pipe: collision detected")
                            sprite.getOutOfPipeG(j)

                    if(j.isFireball()):
                        self.checkF = self.isThereACollision(sprite, j)

                        if(self.checkF == True):
                            sprite.goombaF = True
                            self.sprites.remove(j)

            if(sprite.isChaos()):
                self.fireFrames += 1

                if(self.fireFrames == 20):
                    self.sprites.remove(sprite)
                    self.fireFrames = 0

class View():
    def __init__(self, model):
        screen_size = (800,600)
        self.screen = pygame.display.set_mode(screen_size, 32)
        self.turtle_image = pygame.image.load("mario0.png")
        self.model = model
        
    def update(self):    
        self.screen.fill([255,225,255])
        pygame.draw.line(self.screen, (127,255,0), (10000000000, 0), (0, 600), 100)
   
        for i in range((len(self.model.sprites))):
            if(self.model.sprites[i].isMario()):
                self.scrollPos = self.model.sprites[i].x - 100
    
        for sprite in self.model.sprites:
            sprite.draw(self.screen, self.scrollPos)

        pygame.display.flip()

class Controller():
    def __init__(self, model):
        self.model = model
        self.keep_going = True
        self.key_ctrl = False
        self.scrollPos = 0

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.keep_going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keep_going = False
                if event.key == K_q:
                    self.keep_going = False
                if event.key == K_LCTRL:
                    self.key_ctrl = True
        keys = pygame.key.get_pressed()

        for k in self.model.sprites:
            if(k.isGoomba()):
                k.setPreviousPosition()
                if(k.isCollisionL()):
                    k.x += -8

                if(k.isCollisionR()):
                    k.x += 2

                if(k.goombaF == True):
                    self.model.addChaos(k.x, k.y)
                    self.model.sprites.remove(k)
            
            if((k.isFireball()) and (k.x > self.model.mario.x + 10000)):
                self.model.sprites.remove(k)


        self.model.mario.setPreviousPosition()

        if keys[K_LEFT]:
            self.model.mario.x -= 4
            self.model.mario.walk()
        if keys[K_RIGHT]:
            self.model.mario.x += 4
            self.model.mario.walk()
        if keys[K_SPACE]:
            # print("jump")
            self.model.mario.jump()
        if keys[K_LCTRL]:
            if(self.key_ctrl == True):
                self.key_ctrl = False
                self.model.addFireball()

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
    c.update()
    m.update()
    v.update()
    sleep(0.04)
print("Goodbye")
