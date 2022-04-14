"""A view function takes info from a request and prepares the data needed to generate the page and then sends the
data back to the browser, often by using a template that defines what the page will look like"""
# The file views.py in learning_logs is generated when we ran python manage.py startapp in the terminal

from django.shortcuts import render # This imports the render function, which renders the response based on data
#provided by views

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

"""When a URL request matches the pattern we defined, django looks for a function called index in views.py, and passes 
the request object to this view function. Here we don't need to process any info, so the only code we need is to call 
render(). render() passes two arguments, the orginional request object, and a template it can use to build the page"""
