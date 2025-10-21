from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
from. forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


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

class SinglePostView(View): #replaces post_detail function-based view
    template_name = "blog/post-detail.html"
    model = Post

    def get (self, request, slug):
        identified_post = get_object_or_404(Post, slug=slug) #Fetch a single post by its slug or return 404 if not found
        context = {
            "post": identified_post,
            "tags": identified_post.tags.all(),
            "comment_form": CommentForm, #add an empty comment form to the context
            "comments": identified_post.comments.all().order_by("-id") #fetch all comments related to the post
        }
        return render(request, self.template_name, context)

    def post(self, request, slug): #Handles form submission for comments
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  # Associate the comment with the current post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))  # Redirect to the same page after processing the form
        else:
            identified_post = get_object_or_404(Post, slug=slug)
            context = {
                "post": identified_post,
                "tags": identified_post.tags.all(),
                "comment_form": comment_form, # Return the form with errors
                "comments": identified_post.comments.all().order_by("-id") #fetch all comments related to the post
            }
            return render(request, self.template_name, context)

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts") #use get method to avoid KeyError
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"]) #get post ID from the form data, do not add object directly to session
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")