import pygame.font

class Button(object):
    """description of class"""

    def __init__(self, ai_game, button_caption):
        """Инициализирует свойства кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопки
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._set_caption(button_caption)

    def _set_caption(self, button_caption):
        """Устанавливает надпись на кнопке"""
        self.caption_img = self.font.render(button_caption, True, self.text_color,
                                            self.button_color)
        self.caption_rect = self.caption_img.get_rect()
        self.caption_rect.center = self.rect.center

    def draw_button(self):
        """Отображает кнопку с надписью"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.caption_img, self.caption_rect)



