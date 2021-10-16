from django import forms
from .models import Image,Profile,Comment
from django.contrib.auth.models import User



class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')

