import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from target import Target


class Tetris:
    """  Клас для управления ресурсами и поведением игры."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("TETRIS")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        self.play_button = Button(self, "Play")

    def run_game(self):
        # запуск основноо цикла
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_targets()

            self._update_screen()

    def _ship_hit(self):
        # Если есть попадание в цель
        if self.stats.score_1 < 100:
            self._check_on_target()
            print(self.settings.target_speed)
            self.stats.score_1 += 1
            self.sb.prep_score()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _ship_hit2(self):
        # Если нет попадания в цель
        self.stats.score_2 += 1
        self.sb.prep_score_2()

    def _update_targets(self):
        self._check_fleet_edges()
        self.target.update()

    def _update_bullets(self):
        self.bullets.update()
        # Delite buttets
        for bullet in self.bullets.copy():

            if bullet.rect.left > self.settings.screen_width:
                self._ship_hit2()
                self.bullets.remove(bullet)

        self._check_bullet_target_collis()

    def _check_bullet_target_collis(self):
        # Проверка попадания
        # При попадании в цель.
        collis = pygame.sprite.spritecollide(self.target, self.bullets, True)
        if collis:
            self._ship_hit()

    def _check_events(self):
        # События на клавиатуре
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.stats.game_active = True

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True

            pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_fleet_edges(self):
        """Реагирует на достижение пbришельцем края экрана."""
        if self.target.check_edges():
            self._change_fleet_direction()

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        self.settings.fleet_direction *= -1

    def _check_on_target(self):
        # проверяет количество попаданий если больше пяти увеличивает скорость 
        if self.stats.score_1 != 0:
            if self.stats.score_1 % 5 == 0:
                self.settings.target_speed += 2

    def _update_screen(self):

        # прорисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.target.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображения последнего события на экране
        pygame.display.flip()


if __name__ == '__main__':
    tet = Tetris()
    tet.run_game()
