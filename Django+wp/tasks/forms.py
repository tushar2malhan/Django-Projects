from django import forms
from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 
            'form-control',
            'placeholder': 'Mention Your greetings'}),
        }