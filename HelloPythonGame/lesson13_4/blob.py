import pygame
from pygame.sprite import Sprite

class Blob(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, ai_game):
        """Задаёт начальные настройки для пришельца"""
        super().__init__()

        # Получаем экран
        self.screen = ai_game.screen

        # Получаем Settings
        self.settings = ai_game.settings

        # Загрузка изображения пришельца, настройка изображения и получение его Rect
        self.image = pygame.image.load('lesson13_4/images/blob.bmp')
        self.image = pygame.transform.scale(self.image, (32, 32))

        # Создаём прямоугольник из исходных данных
        self.rect = self.image.get_rect()

        # Установка точки спавна пришельца по умолчанию
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width / 2

        # Запись горизонтальной позиции в виде Float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.spawn_distance_reached = False



    def update(self):
        """Перемещает каплю вниз"""
        self.y += self.settings.blob_down_speed 
        self.rect.y = self.y

    def check_edges(self):
        """Проверяет находится ли капля у края экрана"""
        screen_rect = self.screen.get_rect()
        if (self.rect.bottom >= self.screen_rect.bottom):
            return True

    def can_spawn_new(self):
        """Проверяет прошла ли капля расстояние, чтобы можно было спавнить новую"""
        if self.spawn_distance_reached: return False

        screen_rect = self.screen.get_rect()
        if (self.rect.bottom >= self.screen_rect.bottom - (4 * self.rect.height)):
            self.spawn_distance_reached = True
            return True





