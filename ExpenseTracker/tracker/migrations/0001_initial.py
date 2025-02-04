# Generated by Django 5.1.4 on 2025-01-16 06:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
