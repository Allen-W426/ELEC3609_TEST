# Create a post save signal once a user is created
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# Create a profile once user is created
# Once user creation is saved, send a signal to the receiver for the create_profile() function
# The functions takes in all information signal passed to it, and one of it is instance of user,
# and another one is created message
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # If user is created, create a profile object which user equals to instance of user just created
    if created:
        Profile.objects.create(user=instance)


# Save profile everytime when user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
