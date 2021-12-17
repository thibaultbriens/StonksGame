import pygame

xGraph = 1000
yGraph = 500

prix = [56817, 56957, 56977, 56925, 57120, 57262, 57361, 57539, 57559, 57720, 57890, 57904, 58022, 58050, 58190, 58096, 58110, 58302, 58432, 58522, 58530, 58720, 58872, 58838, 58912, 59069, 59254, 59176, 59226]

pygame.init()

screen = pygame.display.set_mode((1600 , 900) , pygame.FULLSCREEN)
screen.fill((255 , 255 , 255))

continuer = True

def drawGraph(x , y , list) :
    coef = y/(max(list) - min(list)) #coef prix/pixel
    #positions du premier point
    ypos1 = (max(list) - list[0])*coef
    xpos1 = (1/30)*x
    pygame.draw.rect(screen , (0 , 0 , 0) , (xpos1 , ypos1 , 5 , 5))
    yposlast = ((min(list) - list[len(list) - 1])*-1)*coef
    xposlast = x #=> (30/30)*x
    pygame.draw.rect(screen , (0 , 0 , 0) , (xposlast , yposlast , 5 , 5))
    for i in range (1 , len(list) - 2) : #car on calcul 'manuellement' le premier et le dernier
        if list[i] == max(list) :
            ypos = 5
            xpos = ((i+1)/30)*x
            pygame.draw.rect(screen , (0 , 0 , 0) , (xpos , ypos , 5 , 5))
        if list[i] == min(list) :
            ypos = y - 5
            xpos = ((i+1)/30)*x
            pygame.draw.rect(screen , (0 , 0 , 0) , (xpos , ypos , 5 , 5))
        if i == 1 :
            ypos = ((list[i] - list[i + 1])*-1)*coef #ici on soutstrait le premier élément et le suivant/ on multiplie par -1 car quand soustraction psitive on doit descendre et inversement/puis on multiplie le coef
            xpos = ((i+1)/30)*x
            pygame.draw.rect(screen , (0 , 0 , 0) , (xpos , ypos + ypos1 , 5 , 5))
        else :
            ypos = ((list[i] - list[i + 1])*-1)*coef #ici on soutstrait le premier élément et le suivant/ on multiplie par -1 car quand soustraction psitive on doit descendre et inversement/puis on multiplie le coef
            yposMoins1 = ((list[i - 1] - list[i])*-1)*coef
            xpos = ((i+1)/30)*x
            pygame.draw.rect(screen , (0 , 0 , 0) , (xpos , ypos + yposMoins1 , 5 , 5))

while continuer == True :

    for event in pygame.event.get() :
            #si la croix est pressée
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_F12 :
                    continuer = False

    pygame.draw.rect(screen , (255 , 255 , 255) , (20 , 170 , xGraph , yGraph))
    drawGraph(xGraph , yGraph , prix)
    pygame.display.flip()

pygame.quit()