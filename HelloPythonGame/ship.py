import pygame

class Ship():
    """Класс для управления кораблём"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальное положение"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings
        

        # Загружает изображение корабля
        self.image = pygame.image.load('images/ships/ship_34.bmp')

        # Настройка размера изображения корабля
        self.image = pygame.transform.scale(self.image, (96, 96))

        # Считывание четырёхугольника корабля
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется внизу экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение координаты центра корабля
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.b_moving_right = False
        self.b_moving_left = False

    def update(self):
        """Обновляет позицию корабля"""
        if (self.b_moving_right) and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        elif (self.b_moving_left) and (self.rect.left > self.screen_rect.left):
            self.x -= self.settings.ship_speed
        # Обновление атрибута Rect на основе float от self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)