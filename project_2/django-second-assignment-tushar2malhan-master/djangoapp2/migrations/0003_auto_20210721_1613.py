# Generated by Django 3.2.4 on 2021-07-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp2', '0002_auto_20210721_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='last_feed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='last_feed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
