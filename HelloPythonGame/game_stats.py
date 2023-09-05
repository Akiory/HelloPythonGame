import pygame
from game_types import GameStates

class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.setting = ai_game.settings
        self.screen = ai_game.screen
        self.reset_stats()
        self.game_state = GameStates.Play
        
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
        # Установка центра экрана для Rect GameOver-а
        self.game_over_rect.center = self.screen.get_rect().center
        # Отображение GAME OVER
        self.screen.blit(self.game_over_text, self.game_over_rect)

    def show_pause(self):
        """Устанавливает положение и отображает текст PAUSE"""
        self.game_pause_rect.center = self.screen.get_rect().center
        # Отображение PAUSE
        self.screen.blit(self.game_pause_text, self.game_pause_rect)


        

