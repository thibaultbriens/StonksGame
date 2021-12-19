import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position
from random import randint
from tkinter import* #librairie pour les pop up
import statistics

from variables import*

#fonction principal pour le menu
def menuScreen() :
    '''
    role: charger l'écran de menu
    entrée: aucune
    output: aucun
    '''
    global icone , continuer , wallet #importation des variables de locales à globales
    while continuer == True:
    #boucle pour détecter les évènement dans pygame
        for event in pygame.event.get() :
            #pour fermer l'écran
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    continuer = False
                #recommencer à la partie en cours
                if event.key == pygame.K_SPACE :
                    mainScreenFreeGame()
                #recommencer une nouvelle partie
                if event.key == pygame.K_TAB :
                    #on enleve tous ce qui est écrit dans les fichiers txt
                    open('wallet.txt' , 'w') 
                    open('walletbtc.txt' , 'w') 
                    open('prixbtc.txt' , 'w')
                    open('jour.txt' , 'w')
                    open('mois.txt' , 'w')
                    open('annee.txt' , 'w')
                    open('logtexts.txt' , 'w')
                    open('monthpricesbtc.txt' , 'w')
                    #on charge une nouvelle liste de prix du bitcoin
                    variationPrixBTC(30)
                    mainScreenFreeGame()
            if event.type == pygame.QUIT :
                    continuer = False
        #les textes
        screen.blit(font2.render('Cliquez TAB pour recommencer une nouvelle partie' , True , couleurBlanc) , (10 , 10))
        screen.blit(font3.render('Attention ! Cela détruira la partie en cours' , True , couleurBlanc) , (10 , 30))
        screen.blit(font2.render('Cliquez sur ESPACE pour continuer la partie en cours' , True , couleurBlanc) , (10 , 100))

        pygame.display.flip()

def ajoutLogText(list , nb) :
    '''
    role: ajouter un élément dans la liste des logTextes et ainsi l'afficher dans l'historique des actions du joueur
    entrées: la liste 'list' en question qui va etre afficher/un élément 'nb' qui sera ajouter
    output: aucun
    '''
    #si la liste n'est pas deja complète :
    if len(list) < 6 :
        list.append('') #on rajoute un élément a la liste pour ajouter un indice à la liste (indice que l'élement à ajouter va utiliser)
        #puis on déplace tous les éléments de la liste vers la droite
        for i in range (len(list) - 1 , 0 , -1) :
            list[i] = list[i - 1]
        #maintenant on ajoute l'element voulus tout à gauche de la liste
        list[0] = nb
    #en cas que la liste est complete on ajoute pas d'élément mais on déplace quand meme les éléments de la liste vers la droite
    else :
        for i in range (len(list) - 1 , 0 , -1) :
            list[i] = list[i - 1]
        list[0] = nb

def addMonthPricesBTC(list , price) :
    '''
    role: ajouter une valeur a la liste des prix du btc sur 1 mois
    entrées: une liste 'list' ou sera stockées les valeurs/une valeur 'price' à ajouter à la liste
    output: aucun
    '''
    #dans le cas que la liste n'est pas encore complète(liste complète quand il y a 30 éléments; c'est à dire 1 mois de valeurs)
    if len(list) < 29 :
        list.append(price) #on rajoute un élément a la liste
    #dans le cas que la liste est pleine on décale les élément vers la gauche et on rajoute la valeur voulue en fin de liste
    else :
        for i in range (len(list) - 1) :
            list[i] = list[i + 1]
        list[len(list) - 1] = price

def variationPrixBTC(i) :
    '''
    role: fonction pour faire varier le prix du btc aléatoirement(ici entre -600 et +1200 chaques jours)
    entrée: un integer 'i' correspondant au nombre de valeurs à charger
    output: aucun
    '''
    global prixBTC
    for j in range (i) :
        prixBTC += randint(-600 , 1200)
        addMonthPricesBTC(monthPricesBTC , prixBTC)


#fonctions cliques sur un close trade
def openTrade50() :
    global wallet , logTexts , day , month , year , BTCWallet , prixBTC
    if wallet >= 50 :
        wallet -= 50
        BTCWallet += (50/prixBTC)
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Achat 50$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def openTrade100() :
    global wallet , logTexts , day , month , year , BTCWallet , prixBTC
    if wallet >= 100 :
        wallet -= 100
        BTCWallet += (100/prixBTC)
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Achat 100$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

def openTrade1000() :
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if wallet >= 1000 :
        wallet -= 1000
        BTCWallet += (1000/prixBTC)
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Achat 1000$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

#fonctions clique sur un close trade
def closeTrade50() :
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if BTCWallet >= 50/prixBTC :
        wallet += 50
        BTCWallet -= 50/prixBTC
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Vente 50$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def closeTrade100() :
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if BTCWallet >= 100/prixBTC :
        wallet += 100
        BTCWallet -= 100/prixBTC
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Vente 100$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))
def closeTrade1000() :
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if BTCWallet >= 1000/prixBTC :
        wallet += 1000
        BTCWallet -= 1000/prixBTC
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Vente 1000$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

#fonctins pour avancer le temps
def monthAdvanceClick() :
    global months , month , year , day
    if month == 'décembre' :
        year += 1
        month = 'janvier'
    else :
        month = months[months.index(month) + 1] #on va chercher l'indice du mois actuel dans la liste des mois et on rajoute 1 indice pour avoir le mois d'apres
    variationPrixBTC(30)

#fonction pour le month advance 'global' - c'est a dkre quand en cliquant sur +1 jour on change au final de mois
def monthAdvanceGlobal() :
    global months , month , year , day
    if month == 'décembre' :
        year += 1
        month = 'janvier'
    else :
        month = months[months.index(month) + 1]
    variationPrixBTC(1)

def dayAdvance() :
    global month , day , year
    if month in ['janvier' , 'mars' , 'mai' , 'juillet' , 'août' , 'octobre' , 'décembre'] :
        if day <= 30 :
            day += 1
            variationPrixBTC(1)
        else :
            monthAdvanceGlobal()
            day = 1
    elif month == 'février' :
        if day <= 27 :
            day += 1
            variationPrixBTC(1)
        else :
            monthAdvanceGlobal()
            day = 1
    else :
        if day <= 29 :
            day += 1
            variationPrixBTC(1)
        else :
            monthAdvanceGlobal()
            day = 1

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
        monthAdvanceClick()

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

def drawGraph(X, Y, x, y ,list) :
    global yPrevious
    '''
    role: dessiner le graphique des prix
    inputs: X et Y qui sont les coordonnées de création du rectangle ans lequel on va tracer le graphique/ x et y qui sont les coordonnées du bas du rectangle (x=X+longueur rectangle et y=Y+hauteur du rectangle)/une liste qui sont les valeurs dont on veut faire le graphique
    output:
    '''
    #calcul des variables dont on va avoir besoin pour calculer la position de chaque point
    #minPrix = int(min(list))
    #on définis les coordonnées des 'axes' principaux qui sont le max le min et le milieur du graphique
    yCoordMin = y
    for i in range (len(list) - 1) : #boucle for pour générer tous les points
        '''if list[i] == maxPrix : #condition car on a un y spécial pour le maximum
            yActual = yCoordMax
            coord = [((i+1)/30)*(x-X) , yActual]
        elif list[i] == minPrix :
            yActual = yCoordMin
            coord = [((i+1)/30)*(x-X) , yActual]
        elif list[i] == medianePrix :
            yActual = yCoordMediane
            coord = [((i+1)/30)*(x-X) , yActual]
            pygame.draw.line(screen, (0 , 0, 0), (((i/30)*(x-X)), yPrevious), ((((i+1)/30)*(x-X)), yActual))'''
        
        if i == 0:
            yActual = yCoordMin
            coord = [((i+1)/30)*(x-X) , yActual]
        else:
            if int(list[i]) > int(list[i-1]) :
                yActual = yPrevious - 30
            else:
                yActual = yPrevious + 30
            coord = [((i+1)/30)*(x-X) , yActual]
            pygame.draw.line(screen, (255, 255, 255), (((i/30)*(x-X)), yPrevious), ((((i+1)/30)*(x-X)), yActual))
        pygame.draw.rect(screen , (255, 255, 255) , (coord[0] , coord[1] , 5, 5))
        yPrevious = yActual

#fonction de l'écran du jeu
def mainScreenFreeGame() :
    global screen , continuer , icone , wallet , BTCWallet , prixBTC , day , month , year , logTexts , monthPricesBTC , dayButton
    screen = pygame.display.set_mode((width , height) , pygame.FULLSCREEN)
    pygame.display.set_caption("Stonks Trading Simulation")
    pygame.display.set_icon(icone)
    screen.fill(couleurFond)
    walletTxtRead = open('wallet.txt' , 'r') #ouverture du fichier dans lequel est stocké les valeurs du wallet
    walletBTCTxtRead = open('walletbtc.txt' , 'r') #ouverture du fichier dans lequel est stocké les valeurs du walletBTC
    prixBTCTxtRead = open('prixbtc.txt' , 'r')
    jourTxtRead = open('jour.txt' , 'r')
    moisTxtRead = open('mois.txt' , 'r')
    anneeTxtRead = open('annee.txt' , 'r')
    logTextsTxtRead = open('logtexts.txt' , 'r')
    monthBTCTxtRead = open('monthpricesbtc.txt' , 'r')
    #the wallet
    try : #on essaie de chercher une valeur dans le fichier
        wallet = int(walletTxtRead.read())
    except : #si on trouve pas on reset le montant du wallet
        wallet = 10000
    #the BTC wallet
    try :
        BTCWallet = float(walletBTCTxtRead.read()) #ATTENTION c'est un float et non un int !!
    except :
        BTCWallet = 0
    #the BTC price
    try :
        prixBTC = int(prixBTCTxtRead.read())
    except :
        variationPrixBTC(30) #on charge une liste de 30 variations du prix du btc pour pouvoir fairele graphique des le début
    #the day
    try :
        day = int(jourTxtRead.read())
    except :
        day = 1
    #the month
    try :
        month = months[int(moisTxtRead.read())] #fonctionnement sous forme d'index de la liste de tous les mois car méthode de base ne marchait pas
    except :
        month = 'janvier'
    #the year
    try :
        year = int(anneeTxtRead.read())
    except :
        year = 2020
    #the log texts list
    try:
        for element in logTextsTxtRead:
            # remove linebreak which is the last character of the string
            currentElement = element[:-1]
            # add item to the list
            logTexts.append(currentElement)
    except:
        logTexts = []
    #the monthBTCPrices list
    try:
        for element in monthBTCTxtRead:
            # remove linebreak which is the last character of the string
            currentElement = element[:-1]
            # add item to the list
            monthPricesBTC.append(currentElement)
    except:
        variationPrixBTC()

    while continuer == True:
        screen.fill(couleurFond) #on remet le fond d'écran à chaque fois
        
        dateText = font.render((str(day) + ' ' + month + ' ' + str(year)), True , couleurBlanc)
        dayAdvanceText = font2.render('+1 day' , True , couleurBlanc)
        '''weekAdvanceText = font2.render('+1 week' , True , couleurBlanc)'''
        monthAdvanceText = font2.render('+1 mois' , True , couleurBlanc)
        walletText = font.render(str(wallet) + '$', True, couleurBlanc)
        prixBTCText = font.render((str(prixBTC) + ' USD/BTC'), True, couleurBlanc)
        BTCWalletText = font2.render((str(BTCWallet) + ' BTC (= ' + str(round(BTCWallet*prixBTC , 2)) + ' $)'), True, couleurBlanc)

        #boucle our détecter les évènement dans pygame
        for event in pygame.event.get() :
            #si la croix est pressée
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    walletTxtWrite = open('wallet.txt' , 'w')
                    walletTxtWrite.write(str(wallet))
                    walletBTCTxtWrite = open('walletbtc.txt' , 'w')
                    walletBTCTxtWrite.write(str(BTCWallet)) #on multiplie le résultat car quand on lis le fichier il ne lis pas les chiffres à virgules
                    prixBTCTxtWrite = open('prixbtc.txt' , 'w')
                    prixBTCTxtWrite.write(str(prixBTC))
                    jourTxtWrite = open('jour.txt' , 'w')
                    jourTxtWrite.write(str(day))
                    moisTxtWrite = open('mois.txt' , 'w')
                    moisTxtWrite.write(str(months.index(month))) #on ajoute l'index du mois dans le fichier
                    anneeTxtWrite = open('annee.txt' , 'w')
                    anneeTxtWrite.write(str(year))
                    logTextsTxtWrite = open('logtexts.txt' , 'w')
                    for element in logTexts:
                        logTextsTxtWrite.write(str(element) + "\n")
                    monthBTCTxtWrite = open('monthpricesbtc.txt' , 'w')
                    for element in monthPricesBTC:
                        monthBTCTxtWrite.write(str(element) + "\n")
                    continuer = False
                    icone = icone2
            if event.type == pygame.MOUSEBUTTONDOWN :
                clicksPos()
            
        #éléments du jeu
        ##trading area
        pygame.draw.rect(screen , couleurNoir , (width*0.75 , 0 , width/4 , height))
        ##wallet
        pygame.draw.rect(screen , couleurNoir , (0 , 0 , 350 , 75))
        screen.blit(walletText, (0 , 0))
        screen.blit(BTCWalletText, (0 , 50))
        #date
        pygame.draw.rect(screen, couleurNoir , (width/4 , 10-5 , 400 , 50))
        screen.blit(dateText , (width/4 + 40 , 10))
        ##time advance
        ###1 day
        ###les condition sont la pour crééer une interaction avec les boutons
        if (mouse.position[0] < width/2 - 130 - width/6 + 100) and (mouse.position[0] > width/2 - 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
            pygame.draw.rect(screen , couleurRouge , (width/2 - 130 - width/6 , 60 , 100 , 30))
        else : 
            pygame.draw.rect(screen , couleurNoir , (width/2 - 130 - width/6 , 60 , 100 , 30))
        screen.blit(dayAdvanceText , (width/2 - 130 - width/6 + 5, 60 + 5))
        
        '''###1 week
        pygame.draw.rect(screen , couleurNoir , (width/2 - width/6, 60 , 100 , 30))
        screen.blit(weekAdvanceText , (width/2 - width/6 + 5, 60 + 5))'''
        ###1 month
        if (mouse.position[0] < width/2 + 130 - width/6 + 100) and (mouse.position[0] > width/2 + 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
            pygame.draw.rect(screen , couleurRouge , (width/2 + 130 - width/6, 60 , 100 , 30))
        else:
            pygame.draw.rect(screen , couleurNoir , (width/2 + 130 - width/6, 60 , 100 , 30))
        screen.blit(monthAdvanceText , (width/2 + 130 - width/6 + 5, 60 + 5))
        ##currency
        pygame.draw.rect(screen , couleurNoir , (20 , 100 , 350 , 55))
        screen.blit(prixBTCText, (30 , 110))
        ##graph
        pygame.draw.rect(screen , couleurNoir , (20 , 170 , width*0.72 , height/1.8))
        drawGraph(20, 170, width*0.72 , height/1.8, monthPricesBTC)
        ##trades log
        pygame.draw.rect(screen , couleurNoir , (0 , 170 + height/1.8 + 20 , width - width/4 , height/4))
        #affichage des log text
        for i in range (len(logTexts)) :
            screen.blit((font2.render(logTexts[i], True, couleurBlanc)), (20 , 190 + yLogTexts*i + height/1.8 + 20))

        #tradingbox
        ##opentrade
        pygame.draw.rect(screen , couleurBlanc , (width*0.80 , 250 , 190 , 40))
        screen.blit(openTradeText, (width*0.80 , 250))
        ###montants de trade
        ####50$
        if (mouse.position[0] < width*0.80 + 65) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
            pygame.draw.rect(screen , couleurRouge , (width*0.80 , 300 , 65 , 40))
        else:
            pygame.draw.rect(screen , couleurBlanc , (width*0.80 , 300 , 65 , 40))
        screen.blit(cinquanteDollarText, (width*0.80 , 300))
        ####100$
        if (mouse.position[0] < width*0.85 + 90) and (mouse.position[0] > width*0.85) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
            pygame.draw.rect(screen , couleurRouge , (width*0.85 , 300 , 90 , 40))
        else:
            pygame.draw.rect(screen , couleurBlanc , (width*0.85 , 300 , 90 , 40))
        screen.blit(centDollarText, (width*0.85 , 300))
        ####1000$
        if (mouse.position[0] < width*0.916 + 110) and (mouse.position[0] > width*0.916) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
            pygame.draw.rect(screen , couleurRouge , (width*0.916 , 300 , 110 , 40))
        else:
            pygame.draw.rect(screen , couleurBlanc , (width*0.916 , 300 , 110 , 40))
        screen.blit(milleDollarText, (width*0.916 , 300))

        ##closetrade
        pygame.draw.rect(screen , couleurBlanc , (width*0.80 , 450 , 160 , 40))
        screen.blit(closeTradeText, (width*0.80 , 450))
        ####50$
        if (mouse.position[0] < width*0.80 + 65) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
            pygame.draw.rect(screen , couleurRouge , (width*0.80 , 500 , 65 , 40))
        else:
            pygame.draw.rect(screen , couleurBlanc , (width*0.80 , 500 , 65 , 40))
        screen.blit(cinquanteDollarText, (width*0.80 , 500))
        ####100$
        if (mouse.position[0] < width*0.85 + 90) and (mouse.position[0] > width*0.85) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
            pygame.draw.rect(screen , couleurRouge , (width*0.85 , 500 , 90 , 40))
        else:
            pygame.draw.rect(screen , couleurBlanc , (width*0.85 , 500 , 90 , 40))
        screen.blit(centDollarText, (width*0.85 , 500))
        ####1000$
        if (mouse.position[0] < width*0.916 + 110) and (mouse.position[0] > width*0.916) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
            pygame.draw.rect(screen , couleurRouge , (width*0.916 , 500 , 110 , 40))
        else:
            pygame.draw.rect(screen , couleurBlanc , (width*0.916 , 500 , 110 , 40))
        screen.blit(milleDollarText, (width*0.916 , 500))

        #raffraichit le screen => INDISPENSABLE pour afficher quoque ce soit
        pygame.display.flip()

        '''walletTxtRead.close()
        walletBTCTxtRead.close()
        jourTxtRead.close()
        moisTxtRead.close()
        anneeTxtRead.close()

        walletTxtWrite.close()
        walletBTCTxtWrite.close()
        jourTxtWrite.close()
        moisTxtWrite.close()
        anneeTxtWrite.close()'''