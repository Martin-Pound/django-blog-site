from datetime import date
from django.shortcuts import render

#CONSTANTS
all_posts = [
    {
        "slug": "Surfing-Addiction",
        "image": "Surfing.jpeg",
        "author": "Martin Pound",
        "date": date(2025, 3, 15),
        "title": "Surfing Addiction",
        "excerpt": "Why I wish I never knew the feeling of dropping into a wave.",
        "content": """
            lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
            
            lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
            
            lorwm ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
        """
    },
    {
        "slug": "city-food-tour",
        "image": "city-food.jpg",
        "author": "Jane Smith",
        "date": date(2025, 5, 15),
        "title": "Discovering Culinary Delights",
        "excerpt": "A gastronomic adventure through the city's best eateries and hidden gems.",
        "content": """
            lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
            
            lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
            """
    },
    {
        "slug": "art-gallery-opening",
        "image": "art-gallery.png",
        "author": "Emily Johnson",
        "date": date(2025, 7, 15),
        "title": "Exploring Contemporary Art",
        "excerpt": "An immersive experience into modern art and creativity.",
        "content": """
            lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
            
            lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
            """
    },
]

#FUNCTIONS

def get_date(post):
    return post['date'] #Function to get the date of a post

#VIEWS
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date) #Sort posts by date
    latest_posts = sorted_posts[-3:] #Get the latest 3 posts
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
          "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
