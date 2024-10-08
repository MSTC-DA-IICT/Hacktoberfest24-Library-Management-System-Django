# Generated by Django 5.1.1 on 2024-10-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagementSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True),
        ),
    ]