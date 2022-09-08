from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import user table to model
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author is a foreign key points to User

    # On delete cascade (When user is deleted, their posts should be deleted as well)

    def __str__(self):
        return self.title

    # After creating a post instance,
    # redirect user to the post detail page by the new created post primary key
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
