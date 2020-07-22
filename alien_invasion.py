
import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    #Инициализирует pygame , Settings и обьект экрана

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    #создание корабля
    ship = Ship(screen)
    # Запуск основного цикла игры

    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)




        #Отображение последнего прорисованого экрана
        pygame.display.flip()

run_game()
