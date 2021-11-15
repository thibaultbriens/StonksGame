import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position

#variable globale
couleurFond = [0 , 20 , 50]
couleurTest = [0 , 0 , 0]
couleurTest2 = [255 , 255 , 255]

#initialisation des modules
mouse = Controller()
pygame.init()
font = pygame.font.SysFont('didot.ttc', 54)


width , height = 1600 , 900 #indiquez le nobre de pixel de votre écran

screen = pygame.display.set_mode((width , height) , pygame.FULLSCREEN)

icone = pygame.image.load("stonks.jpg").convert_alpha() #peut utiliser '.convert_alpha()' si l'image choisie a arriere plan transparent

pygame.display.set_caption("Stonks Trading Simulation")
pygame.display.set_icon(icone)
screen.fill(couleurFond)

continuer = True #variable pur continuer le jeu ou non
#textes
openTradeText = font.render('OPEN TRADE', True, couleurTest)
closeTradeText = font.render('CLOSE TRADE', True, couleurTest)


while continuer == True:
    #boucle our détecter les évènement dans pygame
    for event in pygame.event.get() :
        #si la croix est pressée
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_F12 :
                continuer = False
        if event.type == pygame.QUIT :
                continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            #cliques avancement de temps
            ##détection clique sur '1 day advance'
            if (mouse.position[0] < width/2 - 130 - width/6 + 100) and (mouse.position[0] > width/2 - 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
                print('pressed 1 day time advancement')
            ##détection clique sur '1 week advance'
            if (mouse.position[0] < width/2 - width/6 + 100) and (mouse.position[0] > width/2 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
                print('pressed 1 week time advancement')
            ##détection clique sur '1 month advance'
            if (mouse.position[0] < width/2 + 130 - width/6 + 100) and (mouse.position[0] > width/2 + 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
                print('pressed 1 month time advancement')

            #cliques open/close trade
            ##open trade
            if (mouse.position[0] < width*0.80 + 255) and (mouse.position[0] > width*0.80) and (mouse.position[1] > 60) and (mouse.position[1] < 60+40) :
                print('openned a trade')
            if (mouse.position[0] < width*0.80 + 280) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 120 + 40) and (mouse.position[1] > 120) :
                print('closed a trade')


    #éléments du jeu
    ##trading area
    pygame.draw.rect(screen , couleurTest , (width*0.75 , 0 , width/4 , height))
    pygame.draw.rect(screen , couleurTest2 , (width*0.80 , 60 , 255 , 40))
    pygame.draw.rect(screen , couleurTest2 , (width*0.80 , 120 , 280 , 40))

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
    pygame.draw.rect(screen , couleurTest , (0 , 170 + height/1.8 + 20 , width - width/4 , height/4))



    screen.blit(openTradeText, (width*0.80 , 60))
    screen.blit(closeTradeText, (width*0.80 , 120))

    #raffraichit le screen => INDISPENSABLE pour afficher quoque ce soit
    pygame.display.flip()

pygame.quit()