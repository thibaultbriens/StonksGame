import pygame
from random import randint

prixBTC = 50000
monthPricesBTC = []

pygame.init()

screen = pygame.display.set_mode((1600 , 900) , pygame.FULLSCREEN)
screen.fill((0 , 0 , 0))

def addMonthPricesBTC(list , price) :
    if len(list) < 29 :
        list.append(price) #on rajoute un élément a la liste
    else :
        for i in range (len(list) - 1) :
            list[i] = list[i + 1]
        list[len(list) - 1] = price
    print(list)

def variationPrixBTC(i) :
    global prixBTC
    for j in range (i) :
        prixBTC += randint(-100 , 200)
        addMonthPricesBTC(monthPricesBTC , prixBTC)

variationPrixBTC(30)

continuer = True

while continuer :
    for event in pygame.event.get() :
            #si la croix est pressée
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    continuer = False

pygame.quit()