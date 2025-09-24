from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post

#CONSTANTS
#all_posts = []

#FUNCTIONS

def get_date(post):
    return post['date'] #Function to get the date of a post

#VIEWS
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] #Fetch latest 3 posts from the database. "-date" orders by date descending
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date") #Fetch all posts from the database ordered by date descending
    return render(request, "blog/all-posts.html", {
          "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug) #Fetch a single post by its slug or return 404 if not found
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
