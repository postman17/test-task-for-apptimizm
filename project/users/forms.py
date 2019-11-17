from django import forms

from .models import User, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')


class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(label='Birth date', widget=forms.SelectDateWidget)

    class Meta():
        model = UserProfile
        fields = ('dob', 'country', 'city')
