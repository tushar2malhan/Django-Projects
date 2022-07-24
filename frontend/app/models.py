
from secrets import choice
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# create different categories for the articles in choices
CATEGORY_CHOICES = (
    ('Technology', 'Technology'),
    ('Business', 'Business'),
    ('Entertainment', 'Entertainment'),
    ('General', 'General'),
    ('Health', 'Health'),
    ('Science', 'Science'),
    ('Sports', 'Sports'),
    ('Travel', 'Travel'),
    ('World', 'World'),
    ('Politics', 'Politics'),
    )

class Articles(models.Model):

    text = models.TextField( null=True, default='Default text')
    category = models.CharField(max_length=100, choices = CATEGORY_CHOICES, default = CATEGORY_CHOICES[0][0]  )

    class Meta :
        verbose_name_plural = 'Articles '
        ordering = ['id']       

    def __str__(self):
        return str(self.id)  +'  ' + self.text  + '  ' + self.category      

