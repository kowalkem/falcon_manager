from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=32)
    house_number = models.CharField(max_length=16)
    vet_number = models.CharField(max_length=16)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.img.path)
