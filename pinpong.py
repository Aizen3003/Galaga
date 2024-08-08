import pygame
import pygame.freetype as fre
pygame.init()

okno = pygame.display.set_mode([1000, 1000])
ball = pygame.rect.Rect(100, 100, 50, 50)
platform1 = pygame.rect.Rect(450, 30, 100, 30)
platform2 = pygame.rect.Rect(450, 970, 100, 30)
casi = pygame.time.Clock()
ink = fre.Font("kartinki/Тексты.otf", 40)
mus = pygame.mixer.Sound("kartinki/Музяка.wav")
otb = pygame.mixer.Sound("kartinki/Странный звук.wav")
otb.set_volume(0.1)
gol = pygame.mixer.Sound("kartinki/Остановка сердца.wav")
gol.set_volume(0.1)
paus = 1

skorostx = 2
skorosty = 1

play1 = 0
play2 = 0
a = 1
while a < 2:
    sobitia = pygame.event.get()
    for sobi in sobitia:
        if sobi.type == pygame.QUIT:
            a += 1
        if sobi.type == pygame.KEYDOWN:
            if sobi.key == pygame.K_ESCAPE:
                if paus == 1:
                    paus = 0
                else:
                    paus = 1
    
    if paus == 0:
        klawischi = pygame.key.get_pressed()
        if klawischi[pygame.K_RIGHT] == True:
            platform2.x += 3
        elif klawischi[pygame.K_LEFT] == True:
            platform2.x -= 3
        
        result1 = ball.colliderect(platform2)
        if result1 == True:
            skorosty = -1
            otb.play()

        if klawischi[pygame.K_q] is True:
            platform1.x -= 3
        elif klawischi[pygame.K_w] is True:
            platform1.x += 3

        result2 = ball.colliderect(platform1)
        if result2 is True:
            skorosty = + 1
            otb.play()

        ball.x += skorostx
        if ball.right >= 1000:
            skorostx = -2
            otb.play()
        elif ball.x <= 1:
            skorostx = 2
            otb.play()

        ball.y += skorosty
        if ball.bottom >= 1000:
            ball.x = 500
            ball.y = 500
            skorosty = -1
            gol.play()
            play2 += 1
        elif ball.y <= 1:
            ball.x = 500
            ball.y = 500
            skorosty = 1
            gol.play()
            play1 += 1

    okno.fill([255, 255, 255])
    pygame.draw.ellipse(okno, [255, 0, 255], ball)
    pygame.draw.rect(okno, [0, 255, 0], platform1)
    pygame.draw.rect(okno, [0, 255, 0], platform2)
    ink.render_to(okno, [0, 0], str(play2), [0, 0, 0])
    ink.render_to(okno, [0, 50], str(play1), [0, 0, 0])
    pygame.display.flip()
    casi.tick(100)