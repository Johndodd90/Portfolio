from django.views.generic import ListView, DetailView

from .models import Blog


class BlogListView(ListView):
    model = Blog
