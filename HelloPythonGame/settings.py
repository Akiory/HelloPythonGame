class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Устанавливает настройки игры"""
        # Геймплей
        self.dynamic_difficult = True
        self.difficult_one_step = 7
        
        # Параметры экрана
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (39, 19, 56)
        self.b_fullscreen_mode = False

        # Параметры корабля
        self.ship_speed = 1
        self.ship_limit = 2

        # Параметры снаряда
        self.projectile_speed = 2
        self.projectile_width = 3
        self.projectile_height = 15
        self.projectile_color = (60, 60, 60)
        self.projectiles_allowed = 20

        # Параметры флота пришельцев
        self.aliens_count = 5
        self.alien_speed = 1.0
        self.alien_down_speed = 15
        self.fleet_direction = 1


