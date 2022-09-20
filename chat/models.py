from datetime import datetime
from django.db import models
from django.contrib.auth.models import User  # Import user table to model
from django.urls import reverse


# Create your models here.

class ChatRoom(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    seller_invited = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invited_chatter")

    # After creating a chat instance,
    # redirect user to the chat detail page by the new created chat primary key
    def get_absolute_url(self):
        return reverse('chatroom_detail', kwargs={'pk': self.pk})


class Message(models.Model):
    chatRoomID = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    msg_writer = models.ForeignKey(User, related_name="writer", on_delete=models.CASCADE)
    msg_content = models.TextField()
    msg_posted = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ("msg_posted",)
