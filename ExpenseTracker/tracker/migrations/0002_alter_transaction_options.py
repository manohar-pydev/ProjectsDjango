# Generated by Django 5.1.4 on 2025-01-16 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('description',)},
        ),
    ]
