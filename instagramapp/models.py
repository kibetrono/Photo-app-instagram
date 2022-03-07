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

    class Meta:
        ordering = ['-created_on']

    def save_image(self):
        self.save()

    def update_image(self, user, image_name, image_caption, image, profile, likes, comments):
        self.user = user
        self.image_name = image_name
        self.image_caption = image_caption
        self.image = image
        self.profile = profile
        self.likes = likes
        self.comments = comments
        self.save()
