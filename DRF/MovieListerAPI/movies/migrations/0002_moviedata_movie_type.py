# Generated by Django 4.2 on 2025-01-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='movie_type',
            field=models.CharField(default='Action', max_length=200),
        ),
    ]
