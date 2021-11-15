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
screen = pygame.display.set_mode((640, 480))
center_x, center_y = 320, 240

clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
prompt = font.render('Entrez un nombre : ', True, BLUE)
prompt_rect = prompt.get_rect(center=(center_x, center_y))

user_input_value = ""
user_input = font.render(user_input_value, True, GREEN)
user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN :
            if (mouse.position[1] < 320) and (mouse.position[0] > 320):
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        continuer = False
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        user_input_value = user_input_value[:-1]
                    else:
                        user_input_value += event.unicode
                    user_input = font.render(user_input_value, True, GREEN)
                    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

    clock.tick(30)

    screen.fill(0)
    screen.blit(prompt, prompt_rect)
    screen.blit(user_input, user_input_rect)
    pygame.display.flip()

##print("La valeur de l'utilisateur convertie en entier est:", int(user_input_value))

pygame.quit()