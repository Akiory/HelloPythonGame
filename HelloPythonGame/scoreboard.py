import pygame.font 

class Scoreboard():
    """Класс для вывода игровой статистики"""

    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчёта очков"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счёта
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка исходного изображения
        self.prep_score()


    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение"""
        score_str = str(self.stats.game_scores)
        self.score_image = self.font.render(score_str, True,
                                             self.text_color, self.settings.bg_color)
        
        # Вывод счёта в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """Выводит счёт на экран"""
        self.screen.blit(self.score_image, self.score_rect)