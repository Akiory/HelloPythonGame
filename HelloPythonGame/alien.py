import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, ai_game):
        """Задаёт начальные настройки для пришельца"""
        super().__init__()

        # Получаем экран
        self.screen = ai_game.screen

        # Получаем Settings
        self.settings = ai_game.settings

        # Загрузка изображения пришельца, настройка изображения и получение его Rect
        self.image = pygame.image.load('images/ships/alien_ship.bmp')
        self.image = pygame.transform.scale(self.image, (140, 140))
        self.rect = self.image.get_rect()

        # Установка точки спавна пришельца по умолчанию
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width / 2

        # Запись горизонтальной позиции в виде Float
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает пришельца вправо"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Проверяет находится ли пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= self.screen_rect.right) or (self.rect.left <= self.screen_rect.left):
            return True








