from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
from. forms import CommentForm


#VIEWS

class StartingPageView(ListView): #replaces starting_page function-based view
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-date")[:3] #Fetch latest 3 posts from the database. "-date" orders by date descending
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3] #Fetch latest 3 posts from the database. "-date" orders by date descending
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class AllPostsView(ListView): #replaces posts function-based view
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"] #Fetch all posts from the database ordered by date descending
# def posts(request):
#     all_posts = Post.objects.all().order_by("-date") #Fetch all posts from the database ordered by date descending
#     return render(request, "blog/all-posts.html", {
#           "all_posts": all_posts
#     })

class SinglePostView(DetailView): #replaces post_detail function-based view
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs): # Adds extra context (tags) to the template
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm() #add an empty comment form to the context
        return context
# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug) #Fetch a single post by its slug or return 404 if not found
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "tags": identified_post.tags.all()
#     })
