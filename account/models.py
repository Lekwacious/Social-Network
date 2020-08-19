from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
    profilePicture = models.ImageField(default='default.jpg', upload_to='users')
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=30, default='Lagos', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

       




