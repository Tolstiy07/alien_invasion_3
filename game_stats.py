class GameStats():


	# statistics
	def __init__(self,tet_game):
		# Inicial statistics
		self.settings = tet_game.settings
		self.reset_stats()

		self.game_active = False

	def reset_stats(self):
		# Количество попаданий
		self.score_1 = 0
		# Количество промахов
		self.score_2 = 0