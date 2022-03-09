from django.forms import ModelForm
from .models import Image,Comments


class PictureUploadForm(ModelForm):
    class Meta:
        model = Image
        fields =['image_name','image_caption','image']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

