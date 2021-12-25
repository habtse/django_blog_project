from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.
class BlogHomeView(ListView):
    model=Post
    template_name="home.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'