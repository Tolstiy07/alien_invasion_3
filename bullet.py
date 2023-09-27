import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # A class of controllin projetiles fied by a ship.

    def __init__(self, tet_game):
        # Creates a projectile object at the ship's current position.
        super().__init__()
        self.screen = tet_game.screen
        self.settings = tet_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = tet_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        # Displaying a projectile on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
