from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
from .models import Topic   # Imports the model we want to register, Topic
                            # The period tells python to look for models.py in the same directory
admin.site.register(Topic)  # This code tells django to manage our model through the admin site
admin.site.register(Entry)