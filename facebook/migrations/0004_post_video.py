# Generated by Django 5.0 on 2023-12-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_alter_post_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
