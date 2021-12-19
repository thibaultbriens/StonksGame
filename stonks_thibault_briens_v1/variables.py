import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position
from random import randint
from tkinter import* #librairie pour les pop up

#variable globale
couleurFond = [0 , 20 , 50]
couleurNoir = [0 , 0 , 0]
couleurBlanc = [255 , 255 , 255]
couleurRouge = [128, 0 , 32]
months = ['janvier' , 'février' , 'mars' , 'avril' , 'mai' , 'juin' , 'juillet' , 'août' , 'septembre' , 'octobre' , 'novembre' , 'décembre']
width , height = 1600 , 900

#gestion wallet et log texts
wallet = 10000
BTCWallet = 0
yLogTexts = 30
logTexts = []

#gestion de la date
day = 1
month = 'janvier'
year = 2021

#gestion du graphique et du prix du bitcoin
prixBTC = 50000
monthPricesBTC = []

#initialisation des modules
mouse = Controller()
pygame.init()
font = pygame.font.SysFont('didot.ttc', 54)
font2 = pygame.font.SysFont('didot.ttc', 30)
font3 = pygame.font.SysFont('didot.ttc', 22)

#variables globales qui doivent etres appelées après l'initialisation des modules
screen = pygame.display.set_mode((600 , 600))
icone = pygame.image.load("stonks.jpg").convert_alpha() #peut utiliser '.convert_alpha()' si l'image choisie a arriere plan transparent
icone2 = pygame.image.load("fond_noir.jpg")

pygame.display.set_caption("Stonks Trading Simulation")
pygame.display.set_icon(icone)

continuer = True #variable pour continuer le jeu ou non

#textes (forcément apres le pygame.init()
cinquanteDollarText = font.render('50$', True, couleurNoir)
centDollarText = font.render('100$', True, couleurNoir)
milleDollarText = font.render('1000$', True, couleurNoir)
openTradeText = font.render('ACHETER', True, couleurNoir)
closeTradeText = font.render('VENDRE', True, couleurNoir)