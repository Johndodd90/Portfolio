from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path(
        route='',
        view=views.BlogListView.as_view(),
        name='list'
    ),
    path(
        route='comment/',
        view=views.CommentCreateView.as_view(),
        name='comment'
    ),
    path(route='<slug:slug>/',
         view=views.BlogDetailView.as_view(),
         name='detail'
         ),
]
