import pygame


class Ship():
    # Kласс управления кораблем

    def __init__(self, tet_game):
        # Инициализирует корабль и задает его начальную позицию
        self.screen = tet_game.screen
        self.settings = tet_game.settings
        self.screen_rect = tet_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # LEFT
        self.rect.midleft = self.screen_rect.midleft
        # FLAG
        self.moving_down = False
        self.moving_up = False
        # Save coordinates  ship center
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        # DROW the Ship
        self.screen.blit(self.image, self.rect)
