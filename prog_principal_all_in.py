import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position

#variable globale
couleurFond = [0 , 20 , 50]
couleurTest = [0 , 0 , 0]
couleurTest2 = [255 , 255 , 255]

wallet = 5000
yLogTexts = 30
logTexts = ['test' , 'test2']

jour = 14
mois = 'octobre'
annee = 2018
date = str(jour) + ' ' + mois +  ' ' + str(annee)
prixBTC = 100000

#initialisation des modules
mouse = Controller()
pygame.init()
font = pygame.font.SysFont('didot.ttc', 54)
font2 = pygame.font.SysFont('didot.ttc', 30)


width , height = 1600 , 900

screen = pygame.display.set_mode((width , height) , pygame.FULLSCREEN)

icone = pygame.image.load("stonks.jpg").convert_alpha() #peut utiliser '.convert_alpha()' si l'image choisie a arriere plan transparent

pygame.display.set_caption("Stonks Trading Simulation")
pygame.display.set_icon(icone)
screen.fill(couleurFond)

continuer = True #variable pur continuer le jeu ou non
#textes (forcément apres le pygame.init()
cinquanteDollarText = font.render('50$', True, couleurTest)
centDollarText = font.render('100$', True, couleurTest)
milleDollarText = font.render('1000$', True, couleurTest)
openTradeText = font.render('OPEN TRADE', True, couleurTest)
closeTradeText = font.render('CLOSE TRADE', True, couleurTest)

'''fonction pour ajouter un nombre dans la liste logText
dépendances : une valeur (string obligatoire) et une liste'''
def ajoutLogText(list , nb) :
    if len(list) < 6 :
        list.append('') #on rajoute un élément a la liste
        for i in range (len(list) - 1 , 0 , -1) :
            list[i] = list[i - 1]
        list[0] = nb
    else :
        for i in range (len(list) - 1 , 0 , -1) :
            list[i] = list[i - 1]
        list[0] = nb

#fonctions cliques sur un close trade
def openTrade50() :
    global wallet , logTexts
    wallet -= 50
    ajoutLogText(logTexts , 'Achat 50$ - BTC/UDS (acheté à ' + str(prixBTC) + '$) - ' + date)
def openTrade100() :
    global wallet , logTexts
    wallet -= 100
    ajoutLogText(logTexts , 'Achat 100$ - BTC/UDS (acheté à ' + str(prixBTC) + '$) - ' + date)
def openTrade1000() :
    global wallet , logTexts
    wallet -= 1000
    ajoutLogText(logTexts , 'Achat 1000$ - BTC/UDS (acheté à ' + str(prixBTC) + '$) - ' + date)

#fonctions clique sur un close trade
def closeTrade50() :
    global wallet , logTexts
    wallet += 50
    ajoutLogText(logTexts , 'Vente 50$ - BTC/UDS (vendu à ' + str(prixBTC) + '$) - ' + date)
def closeTrade100() :
    global wallet , logTexts
    wallet += 100
    ajoutLogText(logTexts , 'Vente 100$ - BTC/UDS (vendu à ' + str(prixBTC) + '$) - ' + date)
def closeTrade1000() :
    global wallet , logTexts
    wallet += 1000
    ajoutLogText(logTexts , 'Vente 1000$ - BTC/UDS (vendu à ' + str(prixBTC) + '$) - ' + date)

def clicksPos() :
    global wallet
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

    #cliques trade box
    #open trades
    ##50$ opentrade
    if (mouse.position[0] < width*0.80 + 65) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
        print('50$ pressed')
        openTrade50()
    ##100$ opentrade
    if (mouse.position[0] < width*0.85 + 90) and (mouse.position[0] > width*0.85) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
        print('100$ pressed')
        openTrade100()
    ##1000$ opentrade
    if (mouse.position[0] < width*0.916 + 110) and (mouse.position[0] > width*0.916) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
        print('1000$ pressed')
        openTrade1000()
    #close trades
    ##50$ closetrade
    if (mouse.position[0] < width*0.80 + 65) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
        print('50$ pressed')
        closeTrade50() #(mettre la fonction de close trade)
    ##100$ closetrade
    if (mouse.position[0] < width*0.85 + 90) and (mouse.position[0] > width*0.85) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
        print('100$ pressed')
        closeTrade100() #(mettre la fonction de close trade)
    ##1000$ closetrade
    if (mouse.position[0] < width*0.916 + 110) and (mouse.position[0] > width*0.916) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
        print('1000$ pressed')
        closeTrade1000() #(mettre la fonction de close trade)

while continuer == True:
    walletText = font.render(str(wallet) + '$', True, couleurTest2)
    
    #boucle our détecter les évènement dans pygame
    for event in pygame.event.get() :
        #si la croix est pressée
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_F12 :
                continuer = False
        if event.type == pygame.QUIT :
                continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            clicksPos()


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
    ##currency
    pygame.draw.rect(screen , couleurTest , (20 , 110 , 100 , 40))
    ##graph
    pygame.draw.rect(screen , couleurTest , (20 , 170 , width*0.72 , height/1.8))
    ##trades log
    pygame.draw.rect(screen , couleurTest , (0 , 170 + height/1.8 + 20 , width - width/4 , height/4))
    #affichage des log text
    for i in range (len(logTexts)) :
        screen.blit((font2.render(logTexts[i], True, couleurTest2)), (20 , 190 + yLogTexts*i + height/1.8 + 20))


    #tradingbox
    ##opentrade
    pygame.draw.rect(screen , couleurTest2 , (width*0.80 , 250 , 255 , 40))
    screen.blit(openTradeText, (width*0.80 , 250))
    ###montants de trade
    ####50$
    pygame.draw.rect(screen , couleurTest2 , (width*0.80 , 300 , 65 , 40))
    screen.blit(cinquanteDollarText, (width*0.80 , 300))
    ####100$
    pygame.draw.rect(screen , couleurTest2 , (width*0.85 , 300 , 90 , 40))
    screen.blit(centDollarText, (width*0.85 , 300))
    ####1000$
    pygame.draw.rect(screen , couleurTest2 , (width*0.916 , 300 , 110 , 40))
    screen.blit(milleDollarText, (width*0.916 , 300))

    ##closetrade
    pygame.draw.rect(screen , couleurTest2 , (width*0.80 , 450 , 280 , 40))
    screen.blit(closeTradeText, (width*0.80 , 450))
    ####50$
    pygame.draw.rect(screen , couleurTest2 , (width*0.80 , 500 , 65 , 40))
    screen.blit(cinquanteDollarText, (width*0.80 , 500))
    ####100$
    pygame.draw.rect(screen , couleurTest2 , (width*0.85 , 500 , 90 , 40))
    screen.blit(centDollarText, (width*0.85 , 500))
    ####1000$
    pygame.draw.rect(screen , couleurTest2 , (width*0.916 , 500 , 110 , 40))
    screen.blit(milleDollarText, (width*0.916 , 500))

    #affichage wallet
    screen.blit(walletText, (0 , 0))

    #raffraichit le screen => INDISPENSABLE pour afficher quoque ce soit
    pygame.display.flip()


pygame.quit()