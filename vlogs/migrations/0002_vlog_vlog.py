# Generated by Django 5.0.7 on 2024-08-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlog',
            name='vlog',
            field=models.FileField(default=2, upload_to='videos/'),
            preserve_default=False,
        ),
    ]
