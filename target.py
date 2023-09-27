import pygame
from pygame.sprite import Sprite

class Target(Sprite):

    def __init__(self, tet_game):
        super().__init__()
        self.screen = tet_game.screen
        self.settings = tet_game.settings
        self.color = self.settings.target_color
        self.screen_rect = tet_game.screen.get_rect()

        self.rect = pygame.Rect(0,0,self.settings.target_width,self.settings.target_height)
        self.rect.midright = self.screen_rect.midright


        self.y = float(self.rect.y)


    
    def blitme(self):
        # DROW the Ship
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        self.y += (self.settings.target_speed * self.settings.fleet_direction)
        self.rect.y = self.y
