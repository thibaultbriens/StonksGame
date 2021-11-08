import pygame

#variable globale
couleurFond = [0 , 20 , 50]
couleurTest = [0 , 0 , 0]

#initialisation du module
pygame.init()

width , height = 1400 , 700

screen = pygame.display.set_mode((width , height))

icone = pygame.image.load("stonks.jpg").convert_alpha() #peut utiliser '.convert_alpha()' si l'image choisie a arriere plan transparent

pygame.display.set_caption("Stonks Trading Simulation")
pygame.display.set_icon(icone)
screen.fill(couleurFond)

continuer = True

while continuer == True:
    #boucle our détecter les évènement dans pygame
    for event in pygame.event.get() :
        #si la croix est pressée
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_F12 :
                continuer = False
        if event.type == pygame.QUIT :
                continuer = False
    #éléments du jeu
    ##trading area
    pygame.draw.rect(screen , couleurTest , (width*0.75 , 0 , width/4 , height))

    ##wallet
    pygame.draw.rect(screen , couleurTest , (0 , 0 , 350 , 35))

    ##time advance
    ###1 day
    pygame.draw.rect(screen , couleurTest , (width/2 - 130 - width/6 , 60 , 100 , 30))
    ###1 week
    pygame.draw.rect(screen , couleurTest , (width/2 - width/6, 60 , 100 , 30))
    ###1 month
    pygame.draw.rect(screen , couleurTest , (width/2 + 130 - width/6, 60 , 100 , 30))

    #currency
    pygame.draw.rect(screen , couleurTest , (20 , 110 , 100 , 40))

    #graph
    pygame.draw.rect(screen , couleurTest , (20 , 170 , width*0.72 , height/1.8))

    #open trades
    pygame.draw.rect(screen , (255 , 255 , 255) , (0 , 170 + height/1.8 + 20 , width - width/4 , height/4))

    #raffraichit le screen => INDISPENSABLE pour afficher quoque ce soit
    pygame.display.flip()

pygame.quit()