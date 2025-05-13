from .models import *
from django import forms

class Details(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    objective = forms.CharField(widget=forms.Textarea)
    # previous_work = forms.CharField(widget=forms.Textarea)
    # skills = forms.CharField(widget=forms.Textarea)