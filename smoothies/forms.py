from django import forms
from .models import Smoothie

class SmoothieForm(forms.ModelForm):
    class Meta:
        model = Smoothie
        fields = ['title', 'description', 'ingredients']
