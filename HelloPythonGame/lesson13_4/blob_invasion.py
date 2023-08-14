import sys
import pygame

from lesson13_4.settings import Settings
from ship import Ship
from projectile import Projectile
from lesson13_4.blob import Blob

class BlobInvasion:
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

        pygame.display.set_caption("Blob Invasion");

        # Создание экземпляра корабля
        self.ship = Ship(self)
        # Создание списка Projectile-ов
        self.projectiles = pygame.sprite.Group()
        # Создание списка пришельцев
        self.blobs = pygame.sprite.Group()

        # Создание флота пришельцев
        self._create_blob_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            
            # Отслеживание событий с клавиатуры
            self._check_events()

            # Обновление корабля
            self.ship.update()

            # Обновление Projectile-ов
            self._update_projectiles()

            # Обновление Blob ships
            self._update_blobs()


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
        self.blobs.draw(self.screen) # Оказывается у класса sprite есть отличный метод draw O_o

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
        #print(len(self.projectiles))

    def _create_blob_fleet(self):
        blob = Blob(self)
        blob_width, blob_height = blob.rect.size
        available_space_x = int(self.settings.screen_width - (1.5 * blob_width))
        max_blobs_inrow = int(available_space_x // (1.5 * blob_width))

        #"""Определяет кол-во рядов помещающихся на экране"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (1.5 * blob_height) - ship_height)
        number_rows = int(available_space_y / (1.5 * blob_height))

        # Создание флота вторжения
        for row_number in range(number_rows):
            for blob_number in range(max_blobs_inrow):
                self._create_blob(blob_number, row_number)

    def _create_blob(self, blob_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        blob = Blob(self)
        blob_width, blob_height = blob.rect.size
        blob.x = blob_width +  1.5 * blob_width * blob_number
        blob.rect.x = blob.x
        blob.y =  1.5 * blob.rect.height * row_number
        self.blobs.add(blob)

    def _update_blobs(self):
        self._check_fleet_edges()
        self.blobs.update()
        
        
        

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for blob in self.blobs.sprites():
            # Можем спавнить новую каплю
            if blob.can_spawn_new():
                self._add_blobs(blob.rect.x, blob.rect.y)
            # Можем удалить старую
            if blob.check_edges():
                self.blobs.remove(blob)
                


    def _add_blobs(self, x_screen_pos, y_screen_pos):
        """Добавляет капли если их нет"""
        blob = Blob(self)
        blob.rect.x = x_screen_pos
        blob.rect.y = y_screen_pos
        self.blobs.add(blob)
   
   

# Создание экземпляра и запуск игры.
ai = BlobInvasion()
ai.run_game()

