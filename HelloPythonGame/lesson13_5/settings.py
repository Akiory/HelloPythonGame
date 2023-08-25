
class Settings:

    def __init__(self):
        
        # Настройка экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (39, 19, 56)

        # Настройка корабля
        self.ship_speed = 1

        # Параметры снаряда
        self.projectile_speed = 2
        self.projectile_width = 3
        self.projectile_height = 15
        self.projectile_color = (60, 60, 60)
        self.projectiles_allowed = 3

        # Параметры флота пришельцев
        self.aliens_count = 5
        self.alien_vertical_speed = 0.5
        self.alien_horizontal_speed = 0.1
        self.alien_down_speed = 10
        self.fleet_direction = 1