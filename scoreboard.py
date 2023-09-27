import pygame.font

class Scoreboard():
	"""Класс для вывода игровой информации."""
	def __init__(self, ai_game):
		"""Инициализирует атрибуты подсчета очков."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Настройки шрифта для вывода счета.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# Подготовка исходного изображения.
		self.prep_score()
		self.prep_score_2()

	def prep_score(self):
		"""Преобразует текущий счет в графическое изображение."""
		score_str = self.stats.score_1
		score_str = f'On target: {"{:,}".format(score_str)}'
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

		# Вывод счета в правой верхней части экрана.
		self.score_rect =  self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 100
		self.score_rect.top = 20

	def prep_score_2(self):
		"""Преобразует текущий счет в графическое изображение."""
		score_str_2 = self.stats.score_2
		score_str_2 = f'Missed the target: {"{:,}".format(score_str_2)}'
		self.score_image_2 = self.font.render(score_str_2, True, self.text_color, self.settings.bg_color)

		# Вывод счета в правой верхней части экрана.
		self.score_rect_2 =  self.score_image_2.get_rect()
		self.score_rect_2.left = self.screen_rect.left + 100
		self.score_rect_2.top = 20

	def show_score(self):
		"""Выводит счет на экран."""
		# Количество попаданий
		self.screen.blit(self.score_image, self.score_rect)
		# Количество промахов
		self.screen.blit(self.score_image_2, self.score_rect_2)

