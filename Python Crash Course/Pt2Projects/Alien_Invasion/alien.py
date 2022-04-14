import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""
	def __init__(self, ai_game):
		"""Initialize alien and it's starting position"""
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image and set it's rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new Alien near the top left of the screen
		self.rect.x = self.rect.width	# Space to left equal to alien width
		self.rect.y = self.rect.height	# Space from top equal to alien height
											# Do this so it's easier to see
		# Store the alien's exact horizontal position
		self.x = float(self.rect.x)	# Track exact horizontal position and make it a float

