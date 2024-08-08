import pygame
import random
import nastroi as nas
import pygame.freetype as fre

class Korab:
    def __init__(self):
        self.kart = pygame.image.load("kartinki/Корабль.png")
        self.ras1 = self.kart.get_width() / 5
        self.ras2 = self.kart.get_height() / 5
        self.kart = pygame.transform.scale(self.kart, [self.ras1, self.ras2])
        self.rect = pygame.rect.Rect([0, 500], [self.ras1, self.ras2])
        self.rect2 = pygame.rect.Rect([0, 500], [self.ras1/1.5, self.ras2/1.5])
        self.spid = 4
        self.HP = 3
        self.Bal = 0

    def otris(self, okn):
        self.rect2.center = self.rect.center
        okn.blit(self.kart, self.rect)
#        pygame.draw.rect(okn, [100, 100, 100], self.rect2)

    def upraw(self):
        klawischi = pygame.key.get_pressed()
        if klawischi[pygame.K_RIGHT] is True:
            self.rect.x += self.spid
        elif klawischi[pygame.K_LEFT] is True:
            self.rect.x -= self.spid

class Metior:
    def __init__(self):
        self.kart = pygame.image.load("kartinki/Метеор.png")
        dell = random.randint(3, 6)
        self.ras1 = self.kart.get_width() / dell
        self.ras2 = self.kart.get_height() / dell
        spavn = random.randint(0, nas.SCHIR)
        self.kart = pygame.transform.scale(self.kart, [self.ras1, self.ras2])
        self.rect = pygame.rect.Rect([spavn, 0], [self.ras1, self.ras2])
        self.rect2 = pygame.rect.Rect([spavn, 0], [self.ras1/1.5, self.ras2/1.5])
        self.rect2.center = self.rect.center
        self.spidx = random.randint(-1, 1)
        self.spidy = random.randint(2, 4)

    def otris(self, okn):
        okn.blit(self.kart, self.rect)
#        pygame.draw.rect(okn, [100, 100, 100], self.rect2)

    def upraw(self):
        self.rect.x += self.spidx
        self.rect.y += self.spidy
        self.rect2.x += self.spidx
        self.rect2.y += self.spidy

class Laser:
    def __init__(self, koorx, koory):
        self.kart = pygame.image.load("kartinki/Лазер.png")
        self.ras1 = self.kart.get_width() / 4
        self.ras2 = self.kart.get_height() / 4
        self.kart = pygame.transform.scale(self.kart, [self.ras1, self.ras2])
        self.rect = pygame.rect.Rect([koorx, koory], [self.ras1, self.ras2])

    def otris(self, okn):
#       pygame.draw.rect(okn, [100, 100, 100], self.rect)
        okn.blit(self.kart, self.rect)
    
    def upraw(self):
        self.rect.y -= 6

class Klaw:
    def __init__ (self, koorx, koory, nas):
        self.kart = pygame.image.load("Kartinki/assets/PNG/UI/Кнопка.png")
        self.ras1 = self.kart.get_width()
        self.ras2 = self.kart.get_height()
        self.inki = fre.Font("kartinki/Тексты.otf", 40)
        self.kart = pygame.transform.scale(self.kart, [self.ras1, self.ras2])
        self.rect = pygame.rect.Rect([koorx, koory], [self.ras1, self.ras2])
        self.tekst = self.inki.render(nas, [0, 0, 0])
        self.kartinkatekst = self.tekst[0]
        self.recttekst = self.tekst[1]
        self.recttekst.center = self.rect.center

    def otris(self, okn):
        okn.blit(self.kart, self.rect)
        okn.blit(self.kartinkatekst, self.recttekst)