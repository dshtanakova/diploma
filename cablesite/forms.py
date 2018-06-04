from django import forms
from .models import *

class CableForm(forms.ModelForm):

    class Meta:
        model = Cable
        exclude = [" "]
