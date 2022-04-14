"""Defines URL patterns for learning_logs."""   # Add docstring so we know which urls.py we are working on

from django.urls import path    # import path function which is needed when mapping URLs to views

from . import views # import views module, dot telling python that views.py is same directory as the current urls module

app_name = 'learning_logs'  # Helps django distinguish this urls.py from files of same name in other apps whithin proj
urlpatterns = [ # this variable in the module is a list of individual pages that can be requested in learning logs app
    # Home page
    path('', views.index, name='index'),    # This calls path() function, which needs three arguments
]   # The first one is the string that helps django route the current request properly
# The second argument specifies which function to call in views.py
# The third argument provides the name index for this URL pattern so we can refer to it on other code sections
    # Whenever we want to provide a link to the home page we use this name instead of writing out the URL