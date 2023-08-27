import pygame

class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.setting = ai_game.settings
        self.screen = ai_game.screen
        self.reset_stats()
        self.game_active = True
        
        self.game_text_init()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        # Сброс колличества кораблей игрока (попыток)
        self.ships_left = self.setting.ship_limit
        self.game_scores = 0 

    def game_text_init(self):
        self.text_color = (255, 255, 255)
        self.text_font = pygame.font.SysFont(None, 64)

        self.game_over_text = self.text_font.render("GAME OVER", True, self.text_color)

        # Создаём один раз, чтобы получилось вычислить положение
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
        # Апдейтим тексты здоровья и очков 
        self.health_text = self.text_font.render(f"Health: {self.ships_left}", True, self.text_color)
        self.scores_text = self.text_font.render(f"Scores: {self.game_scores}", True, self.text_color)

        self.screen.blit(self.health_text, self.health_text_pos)
        self.screen.blit(self.scores_text, self.scores_text_pos)

    

    def show_game_over(self):
        # Рассчёт положения GAME OVER
        x_offset = self.game_over_text.get_rect().width / 2
        y_offset = self.game_over_text.get_rect().height / 2
        x_pos = (self.screen.get_rect().width / 2) - x_offset
        y_pos = (self.screen.get_rect().height / 2) - y_offset

        # Отображение GAME OVER если игра закончилась
        self.screen.blit(self.game_over_text, (x_pos, y_pos))

