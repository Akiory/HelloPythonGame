import pygame

from random import randint
from pygame.sprite import Sprite
from damaged_sprite import Damaged_sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, ai_game, random_spawn_y = True):
        """Задаёт начальные настройки для пришельца"""
        super().__init__()

        # Получаем экран
        self.screen = ai_game.screen

        # Получаем Settings
        self.settings = ai_game.settings

        # Загрузка изображения пришельца, настройка изображения и получение его Rect
        self.image = pygame.image.load('images/ships/alien_ship.bmp')
        self.image = pygame.transform.scale(self.image, (140, 140))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        # Установка точки спавна пришельца по умолчанию
        self.screen_rect = self.screen.get_rect()
        # self.rect.y = self.rect.height / 2
        self.rect.midright = self.screen_rect.midright

        # Проверка аргумента
        if random_spawn_y:
            max_y = self.screen_rect.height - self.rect.height / 2
            min_y = self.rect.height / 2
            self.rect.center = (self.rect.x, randint(min_y, max_y))

        # Запись позиции в виде Float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


        # Создание локального направления для этого пришельца
        self.local_direction = self.settings.fleet_direction

        # Установка спрайта повреждения
        self.damaged_sprite = Damaged_sprite(self)
        self.b_is_damaged = False


    def update(self):
        """Перемещает пришельца вниз"""
        self.y += self.settings.alien_vertical_speed * self.local_direction
        self.rect.y = self.y

        if (self.rect.bottom >= self.screen_rect.bottom) or (
            self.rect.top <= self.screen_rect.top):
                self.local_direction = self.local_direction * -1

        self.x -= self.settings.alien_horizontal_speed
        self.rect.x = self.x
        
        if (self.rect.right <= self.screen_rect.left + 50):
            self.kill()
                




        
        

    def check_edges(self):
        """Проверяет находится ли пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= self.screen_rect.right) or (self.rect.left <= self.screen_rect.left):
            return True

    def set_damaged(self):
        """Рисует корабль в текущей позиции"""
        self.b_is_damaged = True
        
        
        









