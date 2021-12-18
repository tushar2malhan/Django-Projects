from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserLoginForm(AuthenticationForm):
    """This class is used to create a new login form"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                'placeholder':'Username',
                                'required': True, 'autofocus' : True}),
                                )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                'placeholder':'Password',
                                'required': True}),
                                )
