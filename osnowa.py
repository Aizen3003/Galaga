import pygame
import nastroi as nas
import spreit as spr
import pygame.freetype as fre
pygame.init()

okno = pygame.display.set_mode([nas.SCHIR, nas.WIS])
casi = pygame.time.Clock()
korab = spr.Korab()
knop = spr.Klaw(650, 450, "Продолжить")
knop2 = spr.Klaw(650, 550, "Заново")
fon = pygame.image.load("kartinki/Фон.png")
fon = pygame.transform.scale(fon, [nas.SCHIR, nas.WIS])
metiori = []
lasirs = []
ink = fre.Font("kartinki/Тексты.otf", 40)
mus = pygame.mixer.Sound("kartinki/Музяка.wav")
mus.set_volume(0.1)
pli = pygame.mixer.Sound("kartinki/Выстрел.wav")
pli.set_volume(0.1)
paus = 1

sobitie = pygame.USEREVENT
pygame.time.set_timer(sobitie, 1000)
a = 1
#mus.play(-1)
while a < 2:
    sobitia = pygame.event.get()
    for sobi in sobitia:
        if sobi.type == pygame.QUIT:
            a += 1
        if sobi.type == sobitie and paus == 0:
            meti = spr.Metior()
            metiori.append(meti)
        if sobi.type == pygame.KEYDOWN:
            if sobi.key == pygame.K_SPACE and paus == 0:
                las = spr.Laser(korab.rect.x, korab.rect.y)
                pli.play()
                lasirs.append(las)
            if sobi.key == pygame.K_ESCAPE:
                if paus == 1:
                    paus = 0
                else:
                    paus = 1
        if sobi.type == pygame.MOUSEBUTTONDOWN and paus == 1:
            if knop.rect.collidepoint(sobi.pos):
                paus = 0
            if knop2.rect.collidepoint(sobi.pos):
                paus = 0
                korab.HP = 3
                korab.Bal = 0
                metiori = []
                lasirs = []
                korab.rect.x = 0
                korab.rect.y = 500

    if paus == 0:
        korab.upraw()

        for sdn in metiori:
            sdn.upraw()

        for spp in lasirs:
            spp.upraw()

        for demm in metiori:
            if korab.rect2.colliderect(demm.rect2):
                korab.HP -= 1
                metiori.remove(demm)

        for emm in metiori:
            for get in lasirs:
                if emm.rect2.colliderect(get.rect):
                    metiori.remove(emm)
                    lasirs.remove(get)
                    korab.Bal += 1
                    break
    
    if korab.HP <= 0:
        paus = 1

    okno.blit(fon, [0, 0])
    if paus == 0:
        for spn in metiori:
            spn.otris(okno)
        for spl in lasirs:
            spl.otris(okno)
    korab.otris(okno)
    if paus == 1:
        knop.otris(okno)
        knop2.otris(okno)
    ink.render_to(okno, [0, 0], str(korab.Bal), [255, 255, 255])
    pygame.display.flip()
    casi.tick(100)
print(korab.Bal)