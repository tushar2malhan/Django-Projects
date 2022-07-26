from django import forms
from django.forms import  Textarea
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
        fields = ('title','created_at', 'updated_at', 
        'abstract', 'affiliations', 'authors', 
        'body', 'journal', 'keywords', 'url',
        'category')
        widgets = {
            'title': Textarea(attrs={'cols': 10, 'rows': 2}),
            'created_at': forms.SelectDateWidget(attrs={'type': 'date'}),
            'updated_at':  forms.SelectDateWidget(attrs={'type': 'date'}),
            'abstract': Textarea(attrs={'cols': 10, 'rows': 2}),
            'affiliations': Textarea(attrs={'cols': 10, 'rows': 2}),
            'authors': Textarea(attrs={'cols': 10, 'rows': 2}),
            'body': Textarea(attrs={'cols': 10, 'rows': 2}),
            'journal': Textarea(attrs={'cols': 10, 'rows': 2}),
            'keywords': Textarea(attrs={'cols': 10, 'rows': 2}),
            'url': Textarea(attrs={'cols': 10, 'rows': 2}),

        }