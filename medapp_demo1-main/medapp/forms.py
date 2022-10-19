from django import forms
from .models import Elder

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Elder
        fields = ('image',)