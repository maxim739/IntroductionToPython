import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class to manage bullets fired from ship"""
	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a bullet rect at (0, 0) and then set correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,	# Create bullet rect attribute
			self.settings.bullet_height)	# Bullet built from scrath from pygame.Rect() class
		self.rect.midtop = ai_game.ship.rect.midtop	# Set bullet midtop attribute to match ship's midtop

		# Store the bullet position as a decimal value
		self.y = float(self.rect.y)	# Store value for bullet y value to make fine adjustment speed

	def update(self):
		"""Move the bullet up the screen"""
		# Update decimal position of the bullet
		self.y -= self.settings.bullet_speed	# Subtract settings.bullet_speed from self.y to get bullet y value
		# Update the rect position
		self.rect.y = self.y	# Use value of self.y to set value of self.rect.y
	
	def draw_bullet(self):	# Call draw bullet when we want to fire a bullet
		"""Draw bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)	# Fill screen defined by bullet.rect with bullet color