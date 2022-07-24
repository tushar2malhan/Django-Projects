from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Articles


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField( required=True )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        ''' email needs to be unique '''
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(' This Email already exists')
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField( required=True )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        ''' email needs to be unique '''
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(' This Email already exists')
        return email



class TaskForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mention Your greetings'}),
        }