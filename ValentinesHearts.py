import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((800,800))

font = pygame.font.Font(None, 74)

pygame.display.set_caption("Happy Valentines!!")

notExiting = True

clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("amogus.wav")
pygame.mixer.music.play()

imposter = pygame.image.load('imposter.png')

def drawHeart(x,y):
    t = 0
    for i in range(200):
        t+=1
        xpos = -32*math.sin(t)*math.sin(t)*math.sin(t)+x
        ypos = -26*math.cos(t)+10*math.cos(2*t)+4*math.cos(3*t)+2*math.cos(4*t)+y
        pygame.draw.circle(screen, (250,0,0), (xpos, ypos), 2)
    

while notExiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notExiting = False

    screen.blit(imposter, (300, 100), (0, 0, 200, 200))

    drawHeart(100,500)
    drawHeart(300,500)
    drawHeart(500,500)
    drawHeart(700,500)
    drawHeart(200,600)
    drawHeart(400,600)
    drawHeart(600,600)

    firstLine = font.render("You can't spell 'SUS'", 1, (255 ,200 ,200))
    screen.blit(firstLine, (150,350))

    secondLine = font.render("without 'US'!", 1, (255 ,200 ,200))
    screen.blit(secondLine, (250,400))

    pygame.display.flip()

pygame.quit()