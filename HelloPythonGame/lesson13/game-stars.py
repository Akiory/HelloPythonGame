import sys
import pygame

from settings import Settings
from ship import Ship
from projectile import Projectile

from lesson13.star import Star
from random import randint

class StarsInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()

        #Создаём экземпляр settings
        self.settings = Settings()
        
        #Создаём ссылку на экран
        if self.settings.b_fullscreen_mode:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion");

        # Создание экземпляра корабля
        self.ship = Ship(self)
        # Создание списка Projectile-ов
        self.projectiles = pygame.sprite.Group()
        # Создание списка пришельцев
        self.stars = pygame.sprite.Group()

        # Создание флота пришельцев
        self._create_star_fleet()


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            
            # Отслеживание событий с клавиатуры
            self._check_events()

            # Обновление корабля
            self.ship.update()

            # Обновление Projectile-ов
            self._update_projectiles()

            # Отрисовка элементов игры
            self._update_screen()

            


    def _check_events(self):
        # Отслеживание событий с клавиатуры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            # Перемещение влево вправо
            # События по отпусканию кнопки
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Событие по нажатию кнопки
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        
        # При каждой итерации бесконечного цикла перерисовывается цвет экрана
        self.screen.fill(self.settings.bg_color)

        # При каждой итерации перерисовывается корабль игрока
        self.ship.blitme()

        # Перерисовка снарядов (Projectile-ов)
        for projectile in self.projectiles.sprites():
            projectile.draw_projectile()
        # Прорисовка флота пришельцев
        self.stars.draw(self.screen) # Оказывается у класса sprite есть отличный метод draw O_o

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


    def _check_keydown_events(self, event):
        # Управление полётом
        if (event.key == pygame.K_RIGHT):
            # Отпускание вправо
            self.ship.b_moving_right = True
        elif (event.key == pygame.K_LEFT):
            # Отпускание влево
            self.ship.b_moving_left = True

        # Выход на кнопку
        if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
            sys.exit(0)

        # Выстрел снарядом (Projectile-ом)
        if (event.key == pygame.K_SPACE):
            self._launch_projectile()



    def _check_keyup_events(self, event):
        # Управление полётом
        if (event.key == pygame.K_RIGHT):
            # Нажатие вправо
            self.ship.b_moving_right = False
        elif (event.key == pygame.K_LEFT):
            # Нажатие влево
            self.ship.b_moving_left = False

    def _launch_projectile(self):
        """Создание нового снаряда и включение его в группу Projectiles"""
        # Ограничение кол-ва проджектайлов на экране
        if (len(self.projectiles) < self.settings.projectiles_allowed):
            new_projectile = Projectile(self)
            self.projectiles.add(new_projectile)

    def _update_projectiles(self):
        """Обновляет позиции снарядов и удаляет снаряды вне экрана"""
        # Вызов метода Update для каждого Projectile в списке Projectiles
        self.projectiles.update()

        # Удаление покинувших экран снарядов
        for projectile in self.projectiles.copy():
            if (projectile.rect.bottom <= 0):
                self.projectiles.remove(projectile)
        print(len(self.projectiles))

    def _create_star_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        max_stars_inrow = available_space_x // (2 * star_width)

        #"""Определяет кол-во рядов помещающихся на экране"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (1.5 * star_height) - ship_height)
        number_rows = int(available_space_y / (1.5 * star_height))

        # Создание флота вторжения
        for row_number in range(number_rows):
            for star_number in range(max_stars_inrow):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width +  2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y =  1.5 * star.rect.height * row_number
        
        # Упражнение 13.2
        self._random_rotator(star)
        self.stars.add(star)
        

    # Упражнение 13.2
    def _random_rotator(self, star):
        """Поворачивает звезду на рандомный угол"""
        random_rotation = randint(-90, 180)
        star.image = pygame.transform.rotate(star.image, random_rotation)

        # Создание пришельца (old)
        #for i in range(self.settings.aliens_count - 1):
            #alien = Alien(self)
            #alien.rect.x += (192 * i )
            #self.aliens.add(alien)
        

# Создание экземпляра и запуск игры.
ai = StarsInvasion()
ai.run_game()

