from django.contrib import admin
from .models import Post  # From the models.py import Post table

# Register your models here.

admin.site.register(Post)  # Register Post table in admin site, so that admin can view and edit posts
