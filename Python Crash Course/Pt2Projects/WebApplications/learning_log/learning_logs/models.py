from django.db import models

# Create your models here.
class Topic(models.Model):	# Create class called topic inheriting from Model, a django included class defining function
	"""A topic the user is learning about"""	# Add two attributes to Topic class
	text = models.CharField(max_length=200)	# This is a CharField, a piece of data made of text
	# You use a charfield when you want to store a small amount of text, like a title or name
	# We have to define it with a definition for how much space it takes up, which here is 200 characters
	date_added = models.DateTimeField(auto_now_add=True)	# DateTimeField attribute to record date and time
	# add auto_now_add=True tells django to set the attribute to the current date an time when users create a new topic
	# Look at https://docs.djangoproject.com/en/2.2/ref/models/fields/ for different kinds of fields you can use
		# Which will be helpful when making your own apps


# Tell django which attribute to use by default when it displays info about a topic
	def __str__(self):	# Calls a str() method to display a simple representation of the model
		"""Return a string representation of the model"""	# Here we write a model that returns the string
		return self.text										# stored in the text attribute

class Entry(models.Model):	# This class inherits from Models class like Topic class
	"""Something specific learned about a topic"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)	# This is a foreignkey instance
	# A foreignkey is a database term to reference another record in the database, which connects each entry to a topic
	# When sjango needs to connect two pieces of data, it uses the key associated with both pieces of information
	# The on_delete=models.Cascade tells django that when the topic is deleted, all associated entries will also be del
	text = models.TextField()	# Here is an instance of TextField
						# This dosen't have a limit because we don't want to eliminate the amount of induvidual entries
	date_added = models.DateTimeField(auto_now_add=True)	# This allows us to order entries based on date+ a timestamp

	class Meta:	# Meta class in entry class to hold extra info about managing the model
			# It allows us to set an attribute to use Entries when it needs to use more than one entry
				# Otherwise django would refer to multiple entries as Entrys
		verbose_name_plural = 'entries'

	def __str__(self):	# this tells django which info to show when refering to induvidual entries
		"""Return a string representation of the model"""
		return f"{self.text[:50]}..."	# Because they are long, tell django to show first 50 characters in the text