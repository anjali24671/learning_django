from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView # Instead of TemplateView
from .models import Post

class HomePageView(ListView):
    # what is our model
    model = Post 

    # what is our template
    template_name = 'home.html'
    # To give custom name to context_object returned by ListView in /views.py
    context_object_name = 'all_posts_list' # new