import sys
import pygame

def run_game():

    #Инициализирует игру и создает обьект окна
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    #  Подпись окна
    pygame.display.set_caption("Alien invasion")

 #Запуск основного цикла игры

    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    #Отображение последнего прорисованого экрана
    pygame.display.flip()

run_game()
