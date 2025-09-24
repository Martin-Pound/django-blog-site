from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Authors"

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Tags"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog", null=True, blank=True)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts") # Foreign key relationship with Author
    tags = models.ManyToManyField(Tag, related_name="posts") # Many-to-many relationship with Tag


    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug]) # URL to access a particular post instance

    def __str__(self):
        return f"{self.title} - {self.author} ({self.date})"

    class Meta:
        verbose_name_plural = "Posts"