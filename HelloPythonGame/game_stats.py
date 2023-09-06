import pygame
from game_types import GameStates

class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.setting = ai_game.settings
        self.screen = ai_game.screen
        self.reset_stats()
        self.game_state = GameStates.Menu
        
        self.game_text_init()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        # Сброс колличества кораблей игрока (попыток)
        self.ships_left = self.setting.ship_limit
        self.game_scores = 0 

    def game_text_init(self):
        """Создаёт переменные с настройками для полей с игровой информацией или HUD"""
        self.text_color = (255, 255, 255)
        self.text_font = pygame.font.SysFont(None, 64)
        self.controls_font = pygame.font.SysFont(None, 48)
        self.controls_font.set_italic(True)

        self.dyn_text_color = list(self.text_color)

        # Создаёт прямоугольник с текстом GameOver
        self.game_over_text = self.text_font.render("GAME OVER", True, self.text_color)
        self.game_over_rect = self.game_over_text.get_rect()

        # Создаёт прямоугольник с текстом Pause
        self.game_pause_text = self.text_font.render("PAUSE", True, self.text_color)
        self.game_pause_rect = self.game_pause_text.get_rect()

        

        # Создаёт прямоугольник с текстом один раз, чтобы получилось вычислить положение
        self.scores_text = self.text_font.render(f"Scores: {self.game_scores}", True, self.text_color)
        

        # Рассчитываем положение полей со здровьем и очками
        
        self.health_text_pos = list(self.screen.get_rect().midtop)
        x_offset = int((self.screen.get_rect().width / 8) * 3.2)

        self.health_text_pos[0] -= x_offset
        self.health_text_pos[1] += 100


        self.scores_text_pos = list(self.screen.get_rect().midtop)
        x_offset = x_offset - self.scores_text.get_rect().width

        self.scores_text_pos[0] += x_offset
        self.scores_text_pos[1] += 100


        # Обновляем текстовые поля с здоровьем и очками
        self.update_game_text()


     

    def update_game_text(self):
        """Обновляет информацию очков и здоровья игрока"""
        # Апдейтим тексты здоровья и очков 
        self.health_text = self.text_font.render(f"Health: {self.ships_left}", True, self.text_color)
        self.scores_text = self.text_font.render(f"Scores: {self.game_scores}", True, self.text_color)

        self.screen.blit(self.health_text, self.health_text_pos)
        self.screen.blit(self.scores_text, self.scores_text_pos)

    

    def show_game_over(self):
        """Устанавливает положение и отображает текст GAME OVER"""
        # Установка расположения на экране для Rect GameOver-а
        self.game_over_rect.center = self.screen.get_rect().center
        # Отображение GAME OVER
        self.screen.blit(self.game_over_text, self.game_over_rect)

    def show_pause(self):
        """Устанавливает положение и отображает текст PAUSE"""
        self.game_pause_rect.center = self.screen.get_rect().center
        # Отображение PAUSE
        self.screen.blit(self.game_pause_text, self.game_pause_rect)

    def show_game_title(self):
        """Отображает заголовок - название игры"""
        # Сдвигаем цвет
        color = self._make_smooth_color(1)

        # Создаёт прямоугольник с текстом названия игры
        self.game_menu_title = self.text_font.render("SPACE INTRUDERS", True, color)
        self.game_menu_title_rect = self.game_menu_title.get_rect()
        # Установка расположения на экране для названия игры
        self.game_menu_title_rect.center = self.screen.get_rect().center
        self.game_menu_title_rect.y = (self.screen.get_rect().height / 2) - 100
        # Отображение названия игры
        self.screen.blit(self.game_menu_title, self.game_menu_title_rect)

    def show_game_controls(self):

        self.game_controls = ["Controls:", "'Arrow keys' - Move", "Space - Fire", "P - Pause", "Q - Quit Game", "Esc - Game menu / Continue"]
        
        for controls_string in self.game_controls:
            controls_string_render = self.controls_font.render(controls_string, True, self.text_color)
            controls_string_rect = controls_string_render.get_rect()
            # Установка расположения на экране
            controls_string_rect.center = self.screen.get_rect().center
            controls_string_rect.y = (self.screen.get_rect().height / 2) + 50 + ( 50 * self.game_controls.index(controls_string) )

            # Отображение
            self.screen.blit(controls_string_render, controls_string_rect)


    def _make_smooth_color(self, shifting_color = 0):
        """Сдвигает R,G или B цвета каждый кадр 0 - R, 1 - G, 2 - B."""
        self.dyn_text_color[shifting_color % 3] = (self.dyn_text_color[shifting_color % 3] + 1) % 255
        return self.dyn_text_color


        

