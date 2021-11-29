import pygame
import pygame
from pygame.font import*
from pynput.mouse import Controller #library to know mouse position

#variable globale
couleurFond = [0 , 20 , 50]
couleurTest = [0 , 0 , 0]
couleurTest2 = [255 , 255 , 255]

#initialisation des modules
mouse = Controller()

BLUE = (40, 120, 230)
GREEN = (40, 230, 120)

pygame.init()
screen = pygame.display.set_mode((1600, 900))

font = pygame.font.SysFont('Comic Sans MS,Arial', 24)

def chart() :
	

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_F12 :
                continuer = False


    pygame.display.flip()

##print("La valeur de l'utilisateur convertie en entier est:", int(user_input_value))

pygame.quit()