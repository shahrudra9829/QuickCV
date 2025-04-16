from .models import *
from django.forms import ModelForm

class Details(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"