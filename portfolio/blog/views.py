from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Category, Comment


class BlogListView(ListView):
    model = Post


class BlogDetailView(DetailView):
    model = Post


class BlogCategoryView(DetailView):
    model = Category


class CommentCreateView(CreateView):
    model = Comment
    fields = [
        'author',
        'body',
    ]
