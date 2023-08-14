class Settings():
    """Класс для хранения всех настроек игры Blob Invasion"""

    def __init__(self):
        """Устанавливает настройки игры"""
        # Параметры экрана
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (39, 19, 56)
        self.b_fullscreen_mode = False

        # Параметры корабля
        self.ship_speed = 1

        # Параметры снаряда
        self.projectile_speed = 1
        self.projectile_width = 3
        self.projectile_height = 15
        self.projectile_color = (60, 60, 60)
        self.projectiles_allowed = 3

        # Параметры флота пришельцев
        self.blobs_count = 5
        self.blob_speed = 1.0
        self.blob_down_speed = 1
        self.fleet_direction = 1


