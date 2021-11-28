import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position
from random import randint

#variable globale
couleurFond = [0 , 20 , 50]
couleurTest = [0 , 0 , 0]
couleurTest2 = [255 , 255 , 255]
months = ['janvier' , 'février' , 'mars' , 'avril' , 'mai' , 'juin' , 'juillet' , 'août' , 'septembre' , 'octobre' , 'novembre' , 'décembre']

#gestion wallet et log texts
wallet = 5000
yLogTexts = 30
logTexts = []

#gestion de la date
day = 11
month = 'octobre'
year = 2018

#gestion graphique et prix currencies
prixBTC = 50000
monthPricesBTC = ['janvier' , 'février' , 'mars' , 'avril' , 'mai' , 'juin' , 'juillet' , 'août' , 'septembre' , 'octobre' , 'novembre' , 'décembre' , 'janvier' , 'février' , 'mars' , 'avril' , 'mai' , 'juin' , 'juillet' , 'août' , 'septembre' , 'octobre' , 'novembre' , 'décembre' , 'janvier' , 'février' , 'mars' , 'avril']

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

#ajouter une ou des valeurs dans monthPricesBTC
#need une liste et une valeur à ajouter
def addMonthPricesBTC(list , price) :
    if len(list) < 29 :
        list.append(price) #on rajoute un élément a la liste
    else :
        for i in range (len(list) - 1) :
            list[i] = list[i + 1]
        list[len(list) - 1] = price
    print(list)
    
#fonction pour faire varier le prix du btc chaque jour
#nedeed une valeur i =au nombre de jour avancé. Exemple : on clique sur + mois ; alors i = 30
def variationPrixBTC(i) :
    global prixBTC
    for j in range (i) :
        prixBTC += randint(-100 , 200)
        addMonthPricesBTC(monthPricesBTC , prixBTC)
        

#fonctions cliques sur un close trade
def openTrade50() :
    global wallet , logTexts , day , month , year
    wallet -= 50
    ajoutLogText(logTexts , 'Achat 50$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def openTrade100() :
    global wallet , logTexts , day , month , year
    wallet -= 100
    ajoutLogText(logTexts , 'Achat 100$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def openTrade1000() :
    global wallet , logTexts, day , month , year
    wallet -= 1000
    ajoutLogText(logTexts , 'Achat 1000$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

#fonctions clique sur un close trade
def closeTrade50() :
    global wallet , logTexts, day , month , year
    wallet += 50
    ajoutLogText(logTexts , 'Vente 50$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def closeTrade100() :
    global wallet , logTexts, day , month , year
    wallet += 100
    ajoutLogText(logTexts , 'Vente 100$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def closeTrade1000() :
    global wallet , logTexts, day , month , year
    wallet += 1000
    ajoutLogText(logTexts , 'Vente 1000$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
    
#fonctins pour avancer le temps
def monthAdvance() :
    global months , month , year , day
    if month == 'décembre' :
        year += 1
        month = 'janvier'
    else :
        month = months[months.index(month) + 1] #on va chercher l'indice du mois actuel dans la liste des mois et on rajoute 1 indice pour avoir le mois d'apres
def dayAdvance() :
    global month , day , year
    if month in ['janvier' , 'mars' , 'mai' , 'juillet' , 'août' , 'octobre' , 'décembre'] :
        if day <= 30 :
            day += 1
        else :
            monthAdvance()
            day = 1
    elif month == 'février' :
        if day <= 27 :
            day += 1
        else :
            monthAdvance()
            day = 1
    else :
        if day <= 29 :
            day += 1
        else :
            monthAdvance()
            day = 1
    variationPrixBTC(1)
            
def clicksPos() :
    global wallet
    #cliques avancement de temps
            ##détection clique sur '1 day advance'
    if (mouse.position[0] < width/2 - 130 - width/6 + 100) and (mouse.position[0] > width/2 - 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
        print('pressed 1 day time advancement')
        dayAdvance()
    ##détection clique sur '1 week advance'
    if (mouse.position[0] < width/2 - width/6 + 100) and (mouse.position[0] > width/2 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
        print('pressed 1 week time advancement')
    ##détection clique sur '1 month advance'
    if (mouse.position[0] < width/2 + 130 - width/6 + 100) and (mouse.position[0] > width/2 + 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
        print('pressed 1 month time advancement')
        monthAdvance()

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

#fonction pour le graphique
def chart() :
    


#on charge une liste de 30 variations du prix du btc pour pouvoir fairele graphique des le début
variationPrixBTC(30)
while continuer == True:
    dateText = font.render((str(day) + ' ' + month + ' ' + str(year)), True , couleurTest2)
    dayAdvanceText = font2.render('+1 day' , True , couleurTest2)
    weekAdvanceText = font2.render('+1 week' , True , couleurTest2)
    monthAdvanceText = font2.render('+1 mois' , True , couleurTest2)
    walletText = font.render(str(wallet) + '$', True, couleurTest2)
    prixBTCText = font.render((str(prixBTC) + ' USD/BTC'), True, couleurTest2)
    
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
    screen.blit(walletText, (0 , 0))
    #date
    pygame.draw.rect(screen, couleurTest , (width/4 , 10-5 , 400 , 50))
    screen.blit(dateText , (width/4 + 40 , 10))
    ##time advance
    ###1 day
    pygame.draw.rect(screen , couleurTest , (width/2 - 130 - width/6 , 60 , 100 , 30))
    screen.blit(dayAdvanceText , (width/2 - 130 - width/6 + 5, 60 + 5))
    '''###1 week
    pygame.draw.rect(screen , couleurTest , (width/2 - width/6, 60 , 100 , 30))
    screen.blit(weekAdvanceText , (width/2 - width/6 + 5, 60 + 5))'''
    ###1 month
    pygame.draw.rect(screen , couleurTest , (width/2 + 130 - width/6, 60 , 100 , 30))
    screen.blit(monthAdvanceText , (width/2 + 130 - width/6 + 5, 60 + 5))
    ##currency
    pygame.draw.rect(screen , couleurTest , (20 , 100 , 350 , 55))
    screen.blit(prixBTCText, (30 , 110))
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

    #raffraichit le screen => INDISPENSABLE pour afficher quoque ce soit
    pygame.display.flip()

pygame.quit()