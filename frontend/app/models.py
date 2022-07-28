from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

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
from django import forms

class Articles(models.Model):
    title = models.CharField(max_length=255,default='Title')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    abstract = models.TextField(default='Abstract')
    affiliations = models.TextField(default='Affiliations')
    authors = models.CharField(max_length=255, default='Authors')
    body = models.TextField(default='Body')
    journal = models.TextField(default='Journal')
    keywords = models.CharField(db_index=True, max_length=255,default='Keywords')
    url = models.CharField(max_length=255, default='url')
    
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='General')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)



    class Meta :
        verbose_name_plural = 'Articles '
        ordering = ['id']       

    def __str__(self):
        return str(self.id)  +'  ' + self.title  + '  ' + self.category      


