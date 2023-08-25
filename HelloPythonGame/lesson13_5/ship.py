import pygame

class Ship:
    """Класс корабля"""
    def __init__(self, ai_game):
        """Инициализирует корабль"""
        self.screen = ai_game.screen

        #Получаем прямоугольник-поле игры
        self.screen_rect = ai_game.screen.get_rect()
        #Получаем настройки игры
        self.settings = ai_game.settings

        #Загружаем изображение корабля
        self.image = pygame.image.load('images/ships/ship_34.bmp')
        
        #Настройка трансформации изображения
        self.image = pygame.transform.scale(self.image, (128, 128))
        #Поворот изображения корабля для горизонтального расположения
        self.image = pygame.transform.rotate(self.image, -90)
        #Записываем Прямоугольник изображения в переменную
        self.rect = self.image.get_rect()

        #Новый корабль появляется у левого края экрана
        self.rect.midleft = self.screen_rect.midleft

        #Сохраняем координату центра корабля
        self.y = float(self.rect.y)

        #Флаги перемещения
        self.b_moving_up = False
        self.b_moving_down = False

    def update(self):
        """Обновляет состояние корабля"""
        if (self.b_moving_up) and (self.rect.top > self.screen_rect.top):
            self.y -= self.settings.ship_speed
        elif (self.b_moving_down) and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.settings.ship_speed
        #Применяем перемещение к спрайту корабля
        self.rect.y = self.y


    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)





