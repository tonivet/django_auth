from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NONE = ''

    SEX_CHOICES = [
        (NONE, ''),
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=NONE, null=True, blank=True)
    city = models.CharField(max_length=55, blank=True, null=True)
    country = models.CharField(max_length=55, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
