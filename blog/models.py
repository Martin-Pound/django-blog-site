from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog", null=True, blank=True)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()


    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug]) # URL to access a particular post instance

    def __str__(self):
        return f"{self.title} - ({self.author})"