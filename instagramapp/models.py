from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField(max_length=1000)
    image = CloudinaryField('image')
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_number = models.IntegerField(default=0)
    comments_number = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    