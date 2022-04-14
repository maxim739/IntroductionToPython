import sys		# Use tools to exit game when player quits
import pygame	# This module contains functions needed to create a game
from Settings import Settings
from Ship import Ship
from Bullet import Bullet # Import bullet
from alien import Alien

class AlienInvasion:
	"""Overall class to manage game assets and behaviors"""
	def __init__(self):
		"""Initialize game, create game resources"""
		pygame.init()	# Initializes background settings needed to run game properly
		self.settings = Settings()	# Create instance of settings and assign it to self.settings

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)	# Pass size (0,0) and parameter pygame.fullscreen for pygame to figure screen dimensions
		self.settings.screen_width = self.screen.get_rect().width	# Use width and height attributes of screen to update settings object
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)	# Make instance of ship after screen is created
								# Self argument refers to current instance of AlienInvasion()
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		#Set background color
		self.bg_color = (230, 230, 230)	# Assign a color to bg_color



	def run_game(self):
		"""Start main loop for the game"""
		while True:		# Continous while loop
			self._check_events()	# Use dot notation to call method from within class
			self.ship.update()
			self._update_bullets()	# When call update update bullets in group
			self._update_screen()
			


	def _check_events(self):	# Make a check events method to check when player closes game
		"""Respond to keypresses and mouse events"""
		#Watch for keyboard and mouse events
		for event in pygame.event.get():	# Event loop that manages screen updates
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:	# Go into block when keypress is detected
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:	# When player removes rightkey moving_right=False
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:	# If the right arrowkey is pressed enter block
			# Move ship to the right
			self.ship.moving_right = True	# Set moving_right to true when pressed
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:	# Call _fire_bullet when spacebar is pressed
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Respond to key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)	# Make an instance of bullet and call it bullet
			self.bullets.add(new_bullet)	# Add to group Bullets() with add() method

	def _update_bullets(self):
		# Update bullet positions
		self.bullets.update()

		#Delete old bullets which have dissapeared
		for bullet in self.bullets.copy():	# Use copy to copy the list of bullets, where we can modify them
			if bullet.rect.bottom <= 0:	# Check to see if bullet has dissapeared above screen
					self.bullets.remove(bullet)	# Remove it from bullets if it has
			# print(len(self.bullets))	# Add a print statment to see if they have disspeared

	def _create_fleet(self):
		"""Create fleet of aliens"""
		# Create an alien and find the number of aliens in a row
		# Spacing between each alien should be equal to one alien width
		alien  = Alien(self)	# Create an alien before we make calculations
		alien_width = alien.rect.width	# Get alien's width from rect attribute and store in alien_width
		avaliable_space_x = self.settings.screen_width - (2 * alien_width)	# Calculate space for aliens
		number_aliens_x = avaliable_space_x // (2 * alien_width)	# Calculate how many aliens fit in space

		# Create first row of aliens
		for alien_number in range(number_aliens_x):	# Counts from 0 to number of aliens we need to make
			self._create_alien(alien_number)

	def _create_alien(self, alien_number):	# Besides self it also needs the alien number thats being createdd
		"""Create an alien and place it in a row"""
			# Create an alien and place it in a row	
		alien = Alien(self)	# Create new alien
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number	# Set x value to place into row
		# Pushed to the right one alien width margin, multiply by two for left margin
		# Multiply space on left and right by its position in row
		alien.rect.x = alien.x
		self.aliens.add(alien)	# Add alien


	def _update_screen(self):
		"""Update images on screen and flip to the new screen"""
		# Redraw screen during each pass of the loop
		self.screen.fill(self.settings.bg_color)	# Fill screen with this color using the fill() method
		self.ship.blitme()	# Call after background so ship is on top of background
		
		for bullet in self.bullets.sprites():	# Check list of bullets 
			bullet.draw_bullet()	# Draws list of bullets on screen with draw_bullet()

		self.aliens.draw(self.screen)	# Draw aliens to screen through the group
								# When draw is called on group, its drawn by position in rect attributs
								# draw() requires one attribute, the surface to draw the elements from the group
		#Make most recently drawn screen visible
		pygame.display.flip()	# Draws screen on each pass of the while loop
									# Also erases old screen

if __name__ == '__main__':		# This block runs when file is called directly
	# Make a game instance, and run the game
	ai = AlienInvasion()
	ai.run_game()	# Runs the file

#pygame.display.set_mode() crates a display window
#object assignmed to self.screen is called a surface, which is where an element can be displayed
#Each element in the game has its own surface where it is displayed
	#The surface returned by display.set_mode represents the entire game window
# An event is an action the user preforms , so event loop is created to handle those tasks
# Use pygame.event_get() to access events python detects
	# This returns a list of events which happened the last time the function was ran
	# Any event will cause loop to run, and if loop is triggered and action is caused
	# E.g when detected 'x' is clicked, if loop triggers program to close
# When elements moved around in game, pygame.display.flip() continously updates screen
# Colors are given on a value of 0-250, in parenthesis (R, G, B)


# Adding a ship image using the blit() method
	# Make sure to use free licensed images
	# Try to use .bmp images because python uses them by default, but others can be used
	# Use transparent background or solid background which can be edited out'


# The check_events() method
# We move code that manages events to a seperate method called _check_events() to simplify run_game
	# This will also isolate the event managment loop


# The _update_screen() method
# This method will move code from run_game which updates the screen into a seperate method


# Respondng to keypresses
# Each press is registered as an event in python in the pygame.event.get() method
# Check in the _check_events() method what to do with each keypress
	# Keypresses are stores as a KEYDOWN event 
# Now we add elif blocks to move ship based on key presses


# Allowing continous movement
# To keep the ship movement pygame has to realise a release of an arrowkey
# Create a movingright state, when keydown is pressed moveright until it has keyup signal
# In the ship class add these flags for ship movement
# Create an update method in alien_invasion to check if the ship is moving