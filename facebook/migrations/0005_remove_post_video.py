# Generated by Django 5.0 on 2023-12-17 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
