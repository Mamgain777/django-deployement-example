from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# Creating User Profile Form

class UserForm(forms.ModelForm):
    # Updating Password
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','first_name')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)