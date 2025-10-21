from symtable import Class

from django.contrib import admin
from django.template.defaulttags import comment

from .models import Post, Author, Tag, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} #automatically populates the slug field based on the title field
    list_filter = ("author", "date", "tags") #adds filters in the admin interface for these fields
    list_display = ("title", "author", "date") #displays these fields in the admin list view

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address") #displays the full name of the author in the admin list view
    search_fields = ("first_name", "last_name") #adds a search bar to search authors by first or last name

class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",) #displays the tag caption in the admin list view

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post") #displays the user name and associated post in the admin list view
    search_fields = ("user_name", "user_email") #adds a search bar to search comments by user name or email

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
