class Settings():
    # Класс хранения настроек
    def __init__(self):
        # Экран
        self.screen_width = 1300
        self.screen_height = 750
        self.bg_color = (0, 230, 230)

        # Настройки корабля
        self.ship_speed = 3

        # Shot parameters
        self.bullet_speed = 10
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # parameters target
        self.target_speed = 1.1
        self.target_width = 15
        self.target_height = 100
        self.target_color = (60, 60, 60)
        self.fleet_direction = 1


