# Generated by Django 5.0 on 2023-12-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0010_rename_user_save_user_id_post_saved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='save',
            name='value',
            field=models.CharField(choices=[('Liked', 'Liked'), ('Like', 'Like')], default='Save', max_length=10),
        ),
    ]