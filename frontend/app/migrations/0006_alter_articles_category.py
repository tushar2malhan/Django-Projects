# Generated by Django 4.0.6 on 2022-07-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_articles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Business', 'Business'), ('Entertainment', 'Entertainment'), ('General', 'General'), ('Health', 'Health'), ('Science', 'Science'), ('Sports', 'Sports'), ('Travel', 'Travel'), ('World', 'World'), ('Politics', 'Politics')], default='1', max_length=100),
        ),
    ]
