# Generated by Django 5.0.7 on 2024-08-16 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_profile_background_pic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]
