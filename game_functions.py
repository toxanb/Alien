import sys
import pygame

def check_events():
    # отслеживание событий клавиатуры и мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen ,ship):
    """обновляет изображение на экране и отобрадает новый экран"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

