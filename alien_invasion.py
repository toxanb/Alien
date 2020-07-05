import sys
import pygame

def run_game():

    #Инициализирует игру и создает обьект окна

    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien invasion")
    # Запуск основного цикла игры
    bg_color = (230, 230, 230)
    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # При каждом проходе цикла перерисовываеться экран
        screen.fill(bg_color)


    #Отображение последнего прорисованого экрана
    pygame.display.flip()

run_game()
