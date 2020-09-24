# undertale stuff whoo

import pygame
import random

pygame.init()

display_width = 800
display_height = 600


white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bad Undertale')
clock = pygame.time.Clock()

heartImage = pygame.image.load('heart.png')
sansImage = pygame.image.load('sans.png')
boneWave = pygame.image.load('bonewave.png')

heart_width = 32
heart_height = 32

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0
y_change = 0

# top left point is (350,275)
# bottom right point is (525,525)
# centre point is (437.5,400)

bonex = random.randrange(0,display_width)
boney = 0
boneyspeed = 20

bonewavex = -854
bonewavey = 0

def sans_intro(bonewavespeed):
    global bonewavex
    global bonewavey
    global x
    global y
    global x_change
    global y_change
    attacking = True
    while attacking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                     x_change = 5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = -5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_change = 5
             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                
        x += x_change
        y += y_change
        gameDisplay.fill(black)
        gameDisplay.blit(heartImage,(x,y))
        gameDisplay.blit(boneWave,(bonewavex,bonewavey))
        bonewavex += bonewavespeed
        
        if bonewavex >= 854:
            attacking = False
        pygame.display.update()
        clock.tick(60)

def boneattack2(boneyspeed):
    attacking = True
    global x
    global y
    global x_change
    global y_change
    global bonex
    global boney
    while attacking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                     x_change = 5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = -5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_change = 5
             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                
        x += x_change
        y += y_change

        gameDisplay.fill(black)
        pygame.draw.polygon(gameDisplay, white, ((bonex+37.5,boney+75),(bonex+62.5,boney+75),(bonex+62.5,boney+125),(bonex+12.5,boney+125),(bonex+12.5,boney+100),(bonex-37.5,boney+100),(bonex-37.5,boney+125),(bonex-87.5,boney+125),(bonex-87.5,boney+75),(bonex-62.5,boney+75),(bonex-62.5,boney-75),(bonex-87.5,boney-75),(bonex-87.5,boney-125),(bonex-37.5,boney-125),(bonex-37.5,boney-100),(bonex+12.5,boney-100),(bonex+12.5,boney-125),(bonex+62.5,boney-125),(bonex+62.5,boney-75),(bonex+37.5,boney-75)))
        gameDisplay.blit(heartImage,(x,y))
        gameDisplay.blit(sansImage,(355,50))
        bonex += 0
        boney += boneyspeed

        if boney-125>display_height:
            boney = 0 - 250
            bonex = random.randrange(0,display_width)
    
        pygame.display.update()
        clock.tick(60)
sans_intro(20)
boneattack2(100)
