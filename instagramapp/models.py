from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images',null=True,blank="True")
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField(max_length=1000)
    image = CloudinaryField('image')
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank="True")
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

    def delete_image(self):
        self.delete()

    def update_caption(self, caption):
        self.image_caption = caption
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        image_res = cls.objects.get(id=id)
        return image_res

    @classmethod
    def search_image(cls, search_term):
        image_search = cls.objects.filter(image_name__icontains=search_term)
        return image_search

    def __str__(self):
        return self.image_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1200, null=True, blank=True)
    profile_photo = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def save_profile(self):
        self.save()

    def update_profile(self, user, bio, profile_photo):
        self.user = user
        self.bio = bio
        self.profile_photo = profile_photo
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_profile_by_user(cls, user):
        profile_output = cls.objects.filter(user=user)
        return profile_output

    def __str__(self):
        return self.user


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def save_likes(self):
        self.save()

    def update_likes(self, user, image):
        self.user = user
        self.image = image
        self.save()

    def delete_likes(self):
        self.delete()

    def __str__(self):
        return self.user


# comments model
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def save_comment(self):
        self.save()

    def update_comment(self, user, image, comment):
        self.user = user
        self.image = image
        self.comment = comment
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment_by_id(cls, id):
        comment_result = cls.objects.get(idna=id)
        return comment_result

    def __str__(self):
        return self.comment
