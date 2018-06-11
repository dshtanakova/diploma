from django import forms
from django.forms import ModelForm
from .models import *

class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['cable_mark', 'destination_to', 'destination_from', 'status', 'cross_section', 'lenght']
