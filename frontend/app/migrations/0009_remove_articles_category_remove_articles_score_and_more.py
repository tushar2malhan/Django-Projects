# Generated by Django 4.0.6 on 2022-07-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_articles_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='category',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='score',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='text',
        ),
        migrations.AddField(
            model_name='articles',
            name='abstract',
            field=models.TextField(default='Abstract'),
        ),
        migrations.AddField(
            model_name='articles',
            name='affiliations',
            field=models.TextField(default='Affiliations'),
        ),
        migrations.AddField(
            model_name='articles',
            name='authors',
            field=models.CharField(default='Authors', max_length=255),
        ),
        migrations.AddField(
            model_name='articles',
            name='body',
            field=models.TextField(default='Body'),
        ),
        migrations.AddField(
            model_name='articles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='journal',
            field=models.TextField(default='Journal'),
        ),
        migrations.AddField(
            model_name='articles',
            name='keywords',
            field=models.CharField(db_index=True, default='Keywords', max_length=255),
        ),
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(default='Title', max_length=255),
        ),
        migrations.AddField(
            model_name='articles',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='url',
            field=models.CharField(default='url', max_length=255),
        ),
    ]