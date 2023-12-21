# views.py in your Django app
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # This will serve the React app
