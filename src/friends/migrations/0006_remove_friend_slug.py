# Generated by Django 4.2.16 on 2024-11-04 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0005_remove_friend_friend_remove_friend_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='slug',
        ),
    ]