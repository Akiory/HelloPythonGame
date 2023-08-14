import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, ai_game):
        """Задаёт начальные настройки для пришельца"""
        super().__init__()

        # Получаем экран
        self.screen = ai_game.screen

        # Загрузка изображения пришельца, настройка изображения и получение его Rect
        self.image = pygame.image.load('lesson13/images/star.bmp')
        self.image = pygame.transform.scale(self.image, (48, 48))

        # Создаём прямоугольник из исходных данных
        self.rect = self.image.get_rect()

        



        # Установка точки спавна пришельца по умолчанию
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width / 2

        # Запись горизонтальной позиции в виде Float
        self.x = float(self.rect.x)







