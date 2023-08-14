import pygame
from pygame.sprite import Sprite

class Projectile(Sprite):
    """Класс для управления снарядами, выпущенными кораблём"""
    def __init__(self, ai_game):
        """Создаёт объект снаряда в текущей позиции корабля"""

        # Вызываем конструктор родителя
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.projectile_color

        # Создание снаряда в позиции (0, 0) и позиционирование
        self.rect = pygame.Rect(0, 0, self.settings.projectile_width,
                                self.settings.projectile_height)
        # Позиционируем Projectile
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        # Обновление позиции снаряда в вещественном формате
        self.y -= self.settings.projectile_speed
        # Обновление позиции прямоугольника
        self.rect.y = self.y
            

    def draw_projectile(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)



        
