import sys
import pygame
from Settings import Settings

def run_game():

    #Инициализирует pygame , Settings и обьект экрана

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    # Запуск основного цикла игры

    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # При каждом проходе цикла перерисовываеться экран
        screen.fill(ai_settings.bg_color)


        #Отображение последнего прорисованого экрана
        pygame.display.flip()

run_game()
