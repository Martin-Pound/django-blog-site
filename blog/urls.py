from django.urls import path
from . import views

url_patterns = [
    path("", views.starting_page, name="starting-page"), # Home page
    path("posts", views.posts, name="post-page"), # All blog posts
    path("posts/<slug:slug>", views.post_detail, name="post-detail"), # Individual post detail
    ]