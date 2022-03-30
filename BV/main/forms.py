from django import forms
from . import models

class UserProfile(forms.ModelForm):
    class Meta:
        model = models.userProfile
        fields = ['user_name', 'user_phone', 'user_address', 'bio', 'user_image']