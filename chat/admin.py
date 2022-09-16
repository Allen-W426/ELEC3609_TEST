from django.contrib import admin
from .models import ChatRoom, Message  # From the models.py import Post table

# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(Message)