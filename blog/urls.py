from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"), # Home page
    path("posts", views.AllPostsView.as_view(), name="post-page"), # All blog posts
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail"), # Individual post detail
    path("read-later", views.ReadLaterView.as_view(), name="read-later"), # Read later functionality
    ]