import sys
import pygame

# Необходимо для импорта штук из этой папки
#sys.path.append('/.../lesson12_6')
from lesson13_5.settings import Settings
from lesson13_5.ship import Ship
from lesson13_5.projectile import Projectile
from lesson13_5.alien import Alien



class Game:
    """Класс с основной штукой игры"""

    def __init__(self):
        """Инициализирует игру"""
        pygame.init()

        self.settings = Settings()

        # Устанавливаем дисплей
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Game For Lesson12_6')

        # Создаём корабель
        self.ship = Ship(self)

        # Создаём группу где будут храниться выпущенные проджектайлы
        self.projectiles = pygame.sprite.Group()

        # Создаём группу с пришельцами
        self.aliens = pygame.sprite.Group()
        # Последний созданный пришелец
        self.last_created_alien = Alien(self)

        # Создаём таймер
        self.clock = pygame.time.Clock()



    def run_game(self):
        """Основной цикл игры"""

        while True:

            #Чекаем события(в т.ч. клавиатуры)
            self._check_events()

            #Обновляем корабль
            self.ship.update()

            #Обновляем проджектайлы
            self._update_projectiles()

            #Обновляем пришельцев
            self._update_aliens()

            #Спавнит пришельцев
            self._spawn_aliens()

            #Проверяет коллизии пришельцев и проджектайлов
            self._check_alien_projectile_collision()

            #Перерисовываем экран
            self._update_screen()
            pygame.display.flip()



    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.ship.blitme()
        
        # Перерисовка проджектайлов
        for projectile in self.projectiles:
            projectile.draw_projectile()

        # Перерисовка спрайтов пришельцев
        self.aliens.draw(self.screen)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Чекаем нажатоклавишные эвенты
                self._check_keydown_events(event)

            if event.type == pygame.KEYUP:
                # Чекаем отпущенноклавишные эвенты
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if (event.key == pygame.K_UP):
            # Действие по нажатию клавиши UP
            self.ship.b_moving_up = True
        elif (event.key == pygame.K_DOWN):
            # Действие по нажатию DOWN
            self.ship.b_moving_down = True

        # Выход из игры
        if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
            sys.exit(0)

        # Выстрел проджектайлом
        if (event.key == pygame.K_SPACE):
            self._launch_projectile()


    def _check_keyup_events(self, event):
        if (event.key == pygame.K_UP):
            # Действие по отжатию клавиши UP)
            self.ship.b_moving_up = False
        if (event.key == pygame.K_DOWN):
            # Действие по отжатию клавиши DOWN)
            self.ship.b_moving_down = False

    def _launch_projectile(self):
        self.new_projectile = Projectile(self)
        self.projectiles.add(self.new_projectile)
        

    def _update_projectiles(self):
        self.projectiles.update()
        
         # Получаем Screen Rect
        self.screen_rect = self.screen.get_rect()
        # Удаление покинувших экран снарядов
        for projectile in self.projectiles.copy():
            if projectile.rect.right >= self.screen_rect.right:
                self.projectiles.remove(projectile)
        # print(len(self.projectiles))

    def _update_aliens(self):
        self.aliens.update()

    def _create_alien(self):
        alien = Alien(self)
        self.aliens.add(alien)
        self.last_created_alien = alien


    def _spawn_aliens(self):
        # Если пришелец прошел путь достаточный для создания следующего следующего
        if (self.last_created_alien.rect.x < (
            self.screen_rect.width - 2.5 * self.last_created_alien.rect.width)) or (
                not bool(self.aliens)):
                    self._create_alien()

    def _check_alien_projectile_collision(self):
        # Удаляет при коллизии Alien и Projectile
        pygame.sprite.groupcollide(self.aliens, self.projectiles, True, True)
        



        



# Создаём экземпляр игры и запускаем его если это основной файл
if __name__ == "__main__":
    game = Game()
    game.run_game()

