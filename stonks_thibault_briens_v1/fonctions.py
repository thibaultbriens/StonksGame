import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position
from random import randint
from tkinter import* #librairie pour les pop up
#importations locales
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
                    mainScreenGame()
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
                    mainScreenGame()
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

#fonctions pour acheter et vendre du btc
def openTrade50() :
    '''
    role: permettre au joueur d'acheter 50$ de bitcoin
    entree: aucune
    output: aucun
    '''
    global wallet , logTexts , day , month , year , BTCWallet , prixBTC
    #on vérifie que l'utilisateur a assez d'argent restant dans son portefeille pour acheter les 50$ de btc
    if wallet >= 50 :
        wallet -= 50 #on enlève les 50$ au portefeuille
        BTCWallet += (50/prixBTC) #puis on ajoute les 50$ multiplié par le prix actuel du btc au portefeuille bitcoin du joueur
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule pour simplifier la lecture
        ajoutLogText(logTexts , 'Achat 50$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year)) #et on ajoute aussi un texte a l'historique des trade grace à la fonction ajoutLogText()

def openTrade100() :
    '''
    role: permettre au joueur d'acheter 100$ de bitcoin
    entree: aucune
    output: aucun
    '''
    global wallet , logTexts , day , month , year , BTCWallet , prixBTC
    if wallet >= 100 :
        wallet -= 100
        BTCWallet += (100/prixBTC)
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Achat 100$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

def openTrade1000() :
    '''
    role: permettre au joueur d'acheter 1000$ de bitcoin
    entree: aucune
    output: aucun
    '''
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if wallet >= 1000 :
        wallet -= 1000
        BTCWallet += (1000/prixBTC)
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Achat 1000$ - BTC/USD (acheté à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

def closeTrade50() :
    '''
    role: permettre au joueur d'de vendre 50$ de bitcoin
    entree: aucune
    output: aucun
    '''
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    #on vérifie que l'utilisateur a bien les bitcoin requis
    if BTCWallet >= 50/prixBTC :
        wallet += 50 #on ajoute donc les 50$ au portefeuille
        BTCWallet -= 50/prixBTC #et o supprime l'équivalent de 50$ en btc
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Vente 50$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year)) #puis on ajoute un logText pour l'historique 

def closeTrade100() :
    '''
    role: permettre au joueur d'de vendre 100$ de bitcoin
    entree: aucune
    output: aucun
    '''
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if BTCWallet >= 100/prixBTC :
        wallet += 100
        BTCWallet -= 100/prixBTC
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Vente 100$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

def closeTrade1000() :
    '''
    role: permettre au joueur d'de vendre 1000$ de bitcoin
    entree: aucune
    output: aucun
    '''
    global wallet , logTexts, day , month , year , BTCWallet , prixBTC
    if BTCWallet >= 1000/prixBTC :
        wallet += 1000
        BTCWallet -= 1000/prixBTC
        BTCWallet = round(BTCWallet , 5) #arrondit à 5 chiffres après la virgule
        ajoutLogText(logTexts , 'Vente 1000$ - BTC/USD (vendu à ' + str(prixBTC) + '$) - ' + str(day) + ' ' + month + ' ' + str(year))

def monthAdvanceClick() :
    '''
    role: avancer le temps d'un mois (fonction appelée uniquement quand le jouer clique directemet sur le bouton pour avancer d'un mois)
    entrée: aucune
    output: aucun
    '''
    global months , month , year , day
    if month == 'décembre' :
        year += 1
        month = 'janvier'
    else :
        month = months[months.index(month) + 1] #on va chercher l'indice du mois actuel dans la liste des mois et on rajoute 1 indice pour avoir le mois d'apres
    variationPrixBTC(30) #et on charge donc 30 nouvelles valeurs du btc

#fonction pour le month advance 'global' - c'est a dkre quand en cliquant sur +1 jour on change au final de mois
def monthAdvanceGlobal() :
    '''
    role: changer de mois (fonction appelée uniquement quand on est au 30eme ou 31eme jour du mois et qu'on doit donc changer de mois car le jouer veut avancer d'1 jour)
    entrée: aucune
    output: aucun
    '''
    global months , month , year , day
    if month == 'décembre' :
        year += 1
        month = 'janvier'
    else :
        month = months[months.index(month) + 1]
    variationPrixBTC(1) #on charge cette fois ci une seule valeur car on ajoute juste un jour 

def dayAdvance() :
    '''
    role: fonction pour faire +1 jour
    entrée: aucune
    output: aucun
    '''
    global month , day , year
    if month in ['janvier' , 'mars' , 'mai' , 'juillet' , 'août' , 'octobre' , 'décembre'] : #ce sont les mois avec 31 jours 
        #si le jour actuel est inférieur ou égal à 30 on a pas besoin de changer de mois donc on ajoute juste un jour
        if day <= 30 :
            day += 1
            variationPrixBTC(1) #et on charge donc une nouvelle valeur du prix du btc
        #dans l'autre cas on change donc de mois et on appelle la fonction 'globale' de changement de mois
        else :
            monthAdvanceGlobal()
            day = 1 #le jour est donc le premier du mois
    elif month == 'février' : #exception avec février qui n'a que 28 jour (on exclus l'information des années bisextiles)
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
    '''
    role: fonction appelée quand l'utilisateur clique qq part => on fait différentes choses en fonction de la position de la souris
    entrée: aucune
    output: aucun
    '''
    global wallet
    #cliques avancement de temps
    ##détection clique sur '1 day advance'
    if (mouse.position[0] < width/2 - 130 - width/6 + 100) and (mouse.position[0] > width/2 - 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
        dayAdvance()
    ##détection clique sur '1 month advance'
    if (mouse.position[0] < width/2 + 130 - width/6 + 100) and (mouse.position[0] > width/2 + 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
        monthAdvanceClick()
    #cliques sur les achats et ventes
    #open trades = achats
    ##50$ opentrade
    if (mouse.position[0] < width*0.80 + 65) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
        openTrade50()
    ##100$ opentrade
    if (mouse.position[0] < width*0.85 + 90) and (mouse.position[0] > width*0.85) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
        openTrade100()
    ##1000$ opentrade
    if (mouse.position[0] < width*0.916 + 110) and (mouse.position[0] > width*0.916) and (mouse.position[1] < 300 + 40) and (mouse.position[1] > 300) :
        openTrade1000()
    #close trades = ventes
    ##50$ closetrade
    if (mouse.position[0] < width*0.80 + 65) and (mouse.position[0] > width*0.80) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
        closeTrade50()
    ##100$ closetrade
    if (mouse.position[0] < width*0.85 + 90) and (mouse.position[0] > width*0.85) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
        closeTrade100() 
    ##1000$ closetrade
    if (mouse.position[0] < width*0.916 + 110) and (mouse.position[0] > width*0.916) and (mouse.position[1] < 500 + 40) and (mouse.position[1] > 500) :
        closeTrade1000() 

def drawGraph(X, Y, x, y ,list) :
    global yPrevious
    '''
    role: dessiner le graphique des prix de 30 jour(= 1 mois)
    entrées: X et Y qui sont les coordonnées de création du rectangle dans lequel on va tracer le graphique/ x et y qui sont les coordonnées du bas du rectangle (x = X+longueur du rectangle et y = Y+hauteur du rectangle)/une liste 'list' qui sont les valeurs dont on veut faire le graphique
    output:
    '''
    #on définis au préalable la valeur minimum du coordonné 'y'
    yCoordMin = y
    for i in range (len(list) - 1) : #boucle for pour générer tous les points nécessaires
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
        #exception pour le premier point
        if i == 0:
            yActual = yCoordMin #le premier point est égla au minimum
            coord = [((i+1)/30)*(x-X) , yActual] #puis on définis le tuple de coordonnées dans une liste
        else:
            #dans tous les autres cas de 'i' on va chercher la valeur 'yPrevious' qui est le coordonnées 'y' du point d'avant et on ajoute 30 si le pris est supérieur à celui d'avant et inversement si l'inverse
            if int(list[i]) > int(list[i-1]) :
                yActual = yPrevious - 30
            else:
                yActual = yPrevious + 30
            coord = [((i+1)/30)*(x-X) , yActual]
            #puis dessine la ligne entre le point d'avant et le point actuel (donc on ne le fait pas pour i=0 mais pour tous les autres points)
            pygame.draw.line(screen, (255, 255, 255), (((i/30)*(x-X)), yPrevious), ((((i+1)/30)*(x-X)), yActual))
        #on dessine le point actuel qui est un carré de coté 5 pixels
        pygame.draw.rect(screen , (255, 255, 255) , (coord[0] , coord[1] , 5, 5)) 
        yPrevious = yActual #on initialise la valeur actuelle comme valeur d'aant pour la prochaine itération

def mainScreenGame() :
    '''
    role: générer l'écran principal et tous les éléments du jeu 
    entrée: aucune
    output: aucun
    '''
    global screen , continuer , icone , wallet , BTCWallet , prixBTC , day , month , year , logTexts , monthPricesBTC
    screen = pygame.display.set_mode((width , height) , pygame.FULLSCREEN) #on définis une nouvele fenêtre par rapport à la fenetre du menu
    pygame.display.set_caption("Stonks Trading Simulation") #le titre du jeu
    pygame.display.set_icon(icone) #le logo du jeu
    screen.fill(couleurFond)
    #on defnis et ouvre tous les fichiers dont in va avoir besoin pour récupérer les données dans les fichiers txt, si il y en a
    walletTxtRead = open('wallet.txt' , 'r') #ouverture du fichier dans lequel est stocké les valeurs du wallet
    walletBTCTxtRead = open('walletbtc.txt' , 'r') 
    prixBTCTxtRead = open('prixbtc.txt' , 'r')
    jourTxtRead = open('jour.txt' , 'r')
    moisTxtRead = open('mois.txt' , 'r')
    anneeTxtRead = open('annee.txt' , 'r')
    logTextsTxtRead = open('logtexts.txt' , 'r')
    monthBTCTxtRead = open('monthpricesbtc.txt' , 'r')
    #on va maitenant utiliser la méthode python 'try/except' qui est que si le 'try' fait une erreur o n fait 'l'except'
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
        variationPrixBTC(30) #on charge une liste de 30 variations du prix du btc pour pouvoir faire le graphique des le début
    #the day
    try :
        day = int(jourTxtRead.read())
    except :
        day = 1
    #the month
    try :
        month = months[int(moisTxtRead.read())] #fonctionnement sous forme d'index de la liste de tous les mois car méthode de base ne marchait pas - on lit l'index du mois par rapport à la liste 'months'
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
            currentElement = element[:-1] #on enlève le retour à la ligne du fichier txt
            logTexts.append(currentElement) #puis on ajoute la valeur dans la liste
    except:
        logTexts = []
    #the monthBTCPrices list
    try:
        for element in monthBTCTxtRead:
            currentElement = element[:-1]
            monthPricesBTC.append(currentElement)
    except:
        variationPrixBTC()

    #boucle du jeu
    while continuer == True:
        screen.fill(couleurFond) #on remet le fond d'écran à chaque fois

        #initialisation des variables de texte
        dateText = font.render((str(day) + ' ' + month + ' ' + str(year)), True , couleurBlanc)
        dayAdvanceText = font2.render('+1 day' , True , couleurBlanc)
        monthAdvanceText = font2.render('+1 mois' , True , couleurBlanc)
        walletText = font.render(str(wallet) + '$', True, couleurBlanc)
        prixBTCText = font.render((str(prixBTC) + ' USD/BTC'), True, couleurBlanc)
        BTCWalletText = font2.render((str(BTCWallet) + ' BTC (= ' + str(round(BTCWallet*prixBTC , 2)) + ' $)'), True, couleurBlanc)

        #boucle pour détecter les évènement dans pygame
        for event in pygame.event.get() :
            #pour quitter le jeu on detecte si le joueur appuie sur F12
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    #si c'est le cas et que donc le joueur quitte le jeu ; on enregistre toutes les données dans des fichiers txt distincts si le joueur veut reprendre la partie plus tard
                    walletTxtWrite = open('wallet.txt' , 'w')
                    walletTxtWrite.write(str(wallet))
                    walletBTCTxtWrite = open('walletbtc.txt' , 'w')
                    walletBTCTxtWrite.write(str(BTCWallet)) 
                    prixBTCTxtWrite = open('prixbtc.txt' , 'w')
                    prixBTCTxtWrite.write(str(prixBTC))
                    jourTxtWrite = open('jour.txt' , 'w')
                    jourTxtWrite.write(str(day))
                    moisTxtWrite = open('mois.txt' , 'w')
                    moisTxtWrite.write(str(months.index(month))) #on ajoute l'index du mois dans le fichier
                    anneeTxtWrite = open('annee.txt' , 'w')
                    anneeTxtWrite.write(str(year))
                    logTextsTxtWrite = open('logtexts.txt' , 'w')
                    #ici on fait des boucles car on a des listes
                    for element in logTexts:
                        logTextsTxtWrite.write(str(element) + "\n") #on ajoute à chaque fois un element et on reviens à la ligne avec '\n'
                    monthBTCTxtWrite = open('monthpricesbtc.txt' , 'w')
                    for element in monthPricesBTC:
                        monthBTCTxtWrite.write(str(element) + "\n")
                    continuer = False
                    icone = icone2 #on fait cela car sinon on voit les éléments du menu screen quand on ferme le jeu
            #lorsque le joueur clique qq part on vérifie notre fonction 'clickPos()
            if event.type == pygame.MOUSEBUTTONDOWN :
                clicksPos()
            
        #ELEMENTS DU JEU
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
        ###les condition sont la pour crééer une interaction avec les boutons :
        ####si le joueur est sur le bouton la couleur du rectangle change
        if (mouse.position[0] < width/2 - 130 - width/6 + 100) and (mouse.position[0] > width/2 - 130 - width/6) and (mouse.position[1] < 60 + 30) and (mouse.position[1] > 60) :
            pygame.draw.rect(screen , couleurRouge , (width/2 - 130 - width/6 , 60 , 100 , 30))
        else : 
            pygame.draw.rect(screen , couleurNoir , (width/2 - 130 - width/6 , 60 , 100 , 30))
        screen.blit(dayAdvanceText , (width/2 - 130 - width/6 + 5, 60 + 5))
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
        for i in range (len(logTexts)) : #on affiche un par un les élements de la liste
            screen.blit((font2.render(logTexts[i], True, couleurBlanc)), (20 , 190 + yLogTexts*i + height/1.8 + 20)) #en changeant les coordonnées de 'y' en fonction de chaque 'i'

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