from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):       #rozszeżenie formularza z biblioteki
    email = forms.EmailField()      #required is True by default

    class Meta:     #to będzie trzymało razem formularz - metody automatycznefo formularza będą pracowac z zadanymi polami
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: #bez '()'
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

