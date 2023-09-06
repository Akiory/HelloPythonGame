import sys
import pygame


from settings import Settings
from ship import Ship
from projectile import Projectile
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard

from game_types import GameStates


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()

        # Инициализируем Таймер
        self.timer = pygame.time.Clock()

        # Создаём экземпляр settings
        self.settings = Settings()

        # Создаём ссылку на экран
        if self.settings.b_fullscreen_mode:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion");

        # Создаём экзэмпляр игровой статистики
        self.stats = GameStats(self)


        #----------Создаём-экземпляр-для-хранения-счёта----------
        self.sb = Scoreboard(self)
        

        # Создание экземпляра корабля
        self.ship = Ship(self)
        # Создание списка Projectile-ов
        self.projectiles = pygame.sprite.Group()
        # Создание списка пришельцев
        self.aliens = pygame.sprite.Group()
        # Уроны
        self.damage_sprites = pygame.sprite.Group()

        # Создание флота пришельцев
        self._create_alien_fleet()

        # Создаём кнопку начать игру 
        self.play_button = Button(self, "New game")

        # Запускаем какафонию :D
        pygame.mixer.music.load('sounds/PewPewOlolo.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)


        

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:

            
            # Отслеживание событий (в т.ч. с клавиатуры)
            self._check_events()

            # Проба кейса
            match self.stats.game_state:
                case GameStates.Play:

                    # Выполняется если игра активна
                    #if self.stats.game_state == Game_states.Play:
                    # Обновление корабля
                    self.ship.update()

                    # Обновление Projectile-ов
                    self._update_projectiles()

                    # Обновление Alien ships
                    self._update_aliens()

                    # Отрисовка элементов игры
                    self._update_screen()

                case GameStates.GameOver:
                    self.stats.show_game_over()
                    pygame.display.flip()

                case GameStates.Menu:
                    self.show_game_menu()
                    pygame.display.flip()

                case GameStates.Pause:
                    self.stats.show_pause()
                    pygame.display.flip()

                



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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

        # Проверка, должен ли отображаться курсор
        self._check_cursor_visibility()


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
        self.aliens.draw(self.screen) # Оказывается у группы класса sprite есть отличный метод draw O_o

        # Прорисовка повреждений
        self.damage_sprites.draw(self.screen)

        # Прорисовка игрового текста
        self.stats.update_game_text()

        #----------Вывод информации о счёте------------
        self.sb.show_score()


        # Отображение последнего прорисованного экрана
        pygame.display.flip()
        


    def _check_keydown_events(self, event):
        """Управление игрой. Выполняет действия по событиям нажатия клавиш"""
        if (event.key == pygame.K_RIGHT):
            # Нажатие вправо
            self.ship.b_moving_right = True
        elif (event.key == pygame.K_LEFT):
            # Нажатие влево
            self.ship.b_moving_left = True


        # Вызов меню
        if (event.key == pygame.K_ESCAPE):
            self.set_to_menu_state()

        # Выход на кнопку
        if (event.key == pygame.K_q):
            sys.exit(0)
        elif (event.key == pygame.K_p):
            self.set_pause()


        # Выстрел снарядом (Projectile-ом)
        if (event.key == pygame.K_SPACE):
            self._launch_projectile()



    def _check_keyup_events(self, event):
        """Управление игрой. Выполняет действия по событиям отпускания клавиш"""
        # Управление полётом
        if (event.key == pygame.K_RIGHT):
            # Отпускание вправо
            self.ship.b_moving_right = False
        elif (event.key == pygame.K_LEFT):
            # Отпускание влево
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
        # print(len(self.projectiles))



        # Проверяем коллизии
        self._check_collision()

        # Проверяем наличие флота пришельцев
        self._check_aliens_avalability()


    def _create_alien_fleet(self):
        """Создаёт флот пришельцев"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = int(self.settings.screen_width - (1.5 * alien_width))
        max_aliens_inrow = int(available_space_x // (1.5 * alien_width))

        # Определяет кол-во рядов помещающихся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (1.5 * alien_height) - ship_height)
        number_rows = int(available_space_y / (1.5 * alien_height))

        # Создание флота вторжения
        for row_number in range(number_rows):
            for alien_number in range(max_aliens_inrow):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width +  1.5 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y =  1.5 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        self.damage_sprites.update()
        self._check_player_collision()
        self._check_aliens_bottom()
        
        

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Передвигает весь флот вниз и меняет направление движения"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_down_speed
        self.settings.fleet_direction *= -1

    def _check_collision(self):
        """Проверяет наличие коллизий между пришельцами и проджектайлами"""
        # Метод groupcollide() возвращает словарь объектов из переданных групп
        # если между объектами из разных групп произошла коллизия. И удаляет их, 
        # если установлены флаги True для каджой группы
        self.collisions = pygame.sprite.groupcollide(
            self.projectiles, self.aliens, True, False)
        # Устанавливаем повреждение для пришельца
        if bool(self.collisions):    
            sprites_collised = self.collisions.copy()
            print(sprites_collised)
            # Т.к. sprites_collised - словарь с ключём Projectile и значением -
            # - в виде списка пришельцев, хитро разворачиваем его:
            for projectile in sprites_collised:
                for alien in sprites_collised[projectile]:
                    # Удаляем пришельца если он повреждён
                    if alien.b_is_damaged:
                        #Убираем повреждения пришельца и "убиваем" его
                        alien.damaged_sprite.kill()
                        alien.kill()
                        # Добавляем очки
                        self.stats.game_scores += 100
                        continue
                    
                    # Добавляем повреждения пришельца в общую группу повреждений
                    alien.set_damaged()
                    self.damage_sprites.add(alien.damaged_sprite)
                    

    def _check_aliens_avalability(self):
        """Создаёт флот, если группа пришельцев пуста"""
        if not self.aliens:
            self.projectiles.empty()
            
            # Динамическая сложность (Повышение сложности)
            if self.settings.dynamic_difficult:
                self.settings.alien_down_speed += self.settings.difficult_one_step
            self._create_alien_fleet()



    def _check_player_collision(self):
        """Проверяет коллизию между игрком и пришельцем"""
        # принимает 2 аргумента, спрайт и группу. В данном случае, 
        # метод перебирает группу alien и возвращает перво-
        # го пришельца столкнувшегося с кораблём 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """Обрабатывает столкновение корабля игрока с пришельцем"""
        # Уменьшение попыток и отключение игры при их отсутствии
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
        else:
            self.stats.game_state = GameStates.GameOver

        # Очистка пришельцев снарядов и спрайтов повреждения
        self.aliens.empty()
        self.projectiles.empty()
        self.damage_sprites.empty()

        # Создание нового флота и размещение корабля игрока в центре
        self._create_alien_fleet()
        self.ship.center_ship()

        # Задержка
        sleep(1)

    def _check_aliens_bottom(self):
        """Проверяет добрались ли пришельцы до нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Выполняется то же самое, что и при столкновении с короаблём
                self._ship_hit()
                break

    def set_pause(self):
        """Устанавливает паузу. Если пауза уже установлена, снимает паузу"""
        if self.stats.game_state == GameStates.Play:
            self.stats.game_state = GameStates.Pause
        elif self.stats.game_state == GameStates.Pause:
            self.stats.game_state = GameStates.Play


    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play"""
       
        # Метод collidepoint отпределяет находится ли точка щелчка в пределах rect
        if self.play_button.rect.collidepoint(mouse_pos) and (
            self.stats.game_state == GameStates.Menu):

            # Сброс статистики, установка состояния игры - Play
            self.stats.reset_stats()
            self.stats.game_state = GameStates.Play

            # Очистка списков пришельцев и снарядов и эффектов
            self.aliens.empty()
            self.projectiles.empty()
            self.damage_sprites.empty()

            # Создание нового флота
            self._create_alien_fleet()
            self.ship.center_ship()

    def _check_cursor_visibility(self):
        """В соответствии с игровыми состояниями устанавливает видимость курсора"""
        if self.stats.game_state == GameStates.Play and pygame.mouse.get_visible():
            pygame.mouse.set_visible(False)
        elif not (self.stats.game_state == GameStates.Play) and not (pygame.mouse.get_visible()):
            pygame.mouse.set_visible(True)


    def show_game_menu(self):
        self.stats.show_game_title()
        self.play_button.draw_button()
        self.stats.show_game_controls()


    def set_to_menu_state(self):
        if (self.stats.game_state == GameStates.Menu):
            self.stats.game_state = GameStates.Play
        elif (self.stats.game_state == GameStates.Play):
            self.stats.game_state = GameStates.Menu




# Создание экземпляра и запуск игры.
ai = AlienInvasion()
ai.run_game()

