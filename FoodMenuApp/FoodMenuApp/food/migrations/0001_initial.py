# Generated by Django 4.2 on 2024-12-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_desc', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
