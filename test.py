import pygame


 
pygame.init()
 
width = 400
height = 400

screen = pygame.display.set_mode((width , height))

stonksImg = pygame.image.load("stonks.jpg").convert_alpha()

continuer = True

def second(continuer) :
    global screen
    screen = pygame.display.set_mode((1600 , 900) , pygame.FULLSCREEN)
    while continuer == True:
    #boucle our détecter les évènement dans pygame
        for event in pygame.event.get() :
            #si la croix est pressée
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    continuer = False
            elif event.type == pygame.QUIT :
                    continuer = False
        pygame.display.flip()

def first(continuer) :
    while continuer == True:
    #boucle our détecter les évènement dans pygame
        for event in pygame.event.get() :
            #si la croix est pressée
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    continuer = False
                if event.key == pygame.K_SPACE :
                    second(continuer)
            if event.type == pygame.QUIT :
                    continuer = False
        
        screen.blit(stonksImg , (-200 , -50))

        pygame.display.flip()
 
first(continuer)

pygame.quit()