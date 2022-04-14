# After choosing image for the ship we will create a class to manage ship characteristics

import pygame

class Ship:
	"""Class to manage the ship"""
	def __init__(self, ai_game):	# ai_game refrences AlienInvasion() instance
									# This gives function access to resources defined in AlienInvasion()
		"""Initialize ship and starting position"""
		self.screen = ai_game.screen	# Assign screen to attributes of Ship for access in class
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()	# Access rect attribute using get_rect()

		#Load the ship image and get it's rect
		self.image = pygame.image.load('images/ship.bmp')	# Loads the image, returns surface assigned to self.image
		self.rect = self.image.get_rect()	# When image is loaded call it to acces rect attribute so we can place it

		# Start each new ship at bottom center of screen
		self.rect.midbottom = self.screen_rect.midbottom	# Uses midbottom attibute to move
															# Uses rect attributes for positioning
		# Store a decimal value for the ship's horizontal position
		self.x = float(self.rect.x)

		#Movement flag
		self.moving_right = False	# Set moving to false initially
		self.moving_left = False

	def update(self):	# Moves ship right if value for self.moving_right is True
		"""update the ship position based on movement flag"""
		# Update ship's x value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update rect object from self.x
		self.rect.x = self.x

	def blitme(self):	# Define blitme method to draw image to screen at specified position
		"""Draw ship current location"""
		self.screen.blit(self.image, self.rect)

# Python creates every element as a rectangle
# When working with rect object you can use x, y coordinates on top, middle, corners of rect for moving it around
	# When centering, use center, centerx, or centery to establish the rect
	# When working with edge, use top, bottom, left attributes
		# Some combine them in midtop, midbottom, midright, midleft
	# When adjusting position, use x and y attributes for top left corner
# In pygame orgin is at top left corner of screen at (0, 0)
# All coordinates refer to game window, not actual screen
