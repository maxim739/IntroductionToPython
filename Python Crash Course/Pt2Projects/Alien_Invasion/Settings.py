#This file stores settings for features in games in one place
class Settings:
	"""A class to store all settings for Alien_Invasion"""

	def __init__(self):
		"""Initialize game settings"""
		# Ship settings
		self.ship_speed = 1.5

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
