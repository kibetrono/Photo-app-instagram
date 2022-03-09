from django.test import TestCase
from .models import Image,Profile,Likes,Comments
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        """Creating a new location and saving it"""
        user = User.objects.create(username='kibet',first_name='rono',last_name='David')

        self.profile=Profile.objects.create(user=user,bio="New description",profile_photo='lorem2.png',created_on=None)
        self.profile.save_profile()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """Testing Save Method"""
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) < 1)

    def tearDown(self):
        """tearDown method"""
        Profile.objects.all().delete()




class ImageTestClass(TestCase):

    def setUp(self):
        """setUp Method"""
        user = User.objects.create(username='kibet',first_name='rono',last_name='David')
        self.image=Image.objects.create(user=user,image_name='snow',image='lorem.png',image_caption='The best image',profile_id=user.id,likes_number=0,comments_number=0,created_on=None)

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.image, Image))


    def test_save_method(self):
        """Testing Save Method"""
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) < 1)

    def tearDown(self):
        """tearDown method"""
        Image.objects.all().delete()



class LikesTestClass(TestCase):

    def setUp(self):
        user = User.objects.create(username='kicbet',first_name='rono',last_name='David')

        self.image=Image.objects.create(user=user,image_name='snow',image='lorem.png',image_caption='The best image',profile_id=user.id,likes_number=0,comments_number=0,created_on=None)

        user = User.objects.create(username='kibet',first_name='rono',last_name='David')
        self.likes = Likes.objects.create(user=user,image=self.image)
        self.likes.save_likes()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.likes, Likes))

    def test_save_method(self):
        """Testing Save Method"""
        self.likes.save_likes()
        likes = Likes.objects.all()
        self.assertTrue(len(likes) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.likes.delete_likes()
        likes = Likes.objects.all()
        self.assertTrue(len(likes) < 1)

    def tearDown(self):
        """tearDown method"""
        Likes.objects.all().delete()


class CommentsTestClass(TestCase):

    def setUp(self):
        user = User.objects.create(username='kicbet',first_name='rono',last_name='David')

        self.image=Image.objects.create(user=user,image_name='snow',image='lorem.png',image_caption='The best image',profile_id=user.id,likes_number=0,comments_number=0,created_on=None)
        user = User.objects.create(username='kibet',first_name='rono',last_name='David')

        self.comments = Comments(user=user,image=self.image,comment="initial comment")
        self.comments.save_comment()

    def test_instance(self):
            """Testing instance"""
            self.assertTrue(isinstance(self.comments, Comments))

    def test_save_method(self):
        """Testing Save Method"""
        self.comments.save_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.comments.delete_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) < 1)

    def tearDown(self):
        """tearDown method"""
        Comments.objects.all().delete()