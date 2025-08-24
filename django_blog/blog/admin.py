from django.contrib import admin
from .models import Post, Comment, Profile  # add Book if you have a Book model

# Register models to show in Django admin
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
# admin.site.register(Book)  # uncomment this if you have a Book model
