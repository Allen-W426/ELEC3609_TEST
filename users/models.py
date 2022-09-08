from django.contrib.auth.models import User
from django.db import models
from PIL import Image  # Import pillow dependency for resize the uploaded images


class Profile(models.Model):
    # If users are deleted in other model, delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Create image attribute,
    # if image not uploaded the defaulted image will be uploaded into profile_pics directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Print out the object in specific format
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
