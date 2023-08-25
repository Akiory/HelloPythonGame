import pygame
from pygame.sprite import Sprite

class Projectile(Sprite):
    """Класс снаряда выпущенного кораблём"""

    def __init__(self, ai_game):
        """Создаёт снаряд в текущей позиции корабля"""
        
        #Вызываем конструктор родителя
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.projectile_color

        #Создаём Rect для снаряда с помощью конструктора
        self.rect = pygame.Rect(0,0, self.settings.projectile_height, self.settings.projectile_width)

        #Позиционируем Rect 
        self.rect.midleft = ai_game.ship.rect.midright

        #Позиция хранится в вещественном формате
        self.x = float(self.rect.x)

    def update(self):
        """перемещает снаряд по экрану"""
        self.x += self.settings.projectile_speed
        # Обновление позиции прямоугольника
        self.rect.x = self.x

    def draw_projectile(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)




