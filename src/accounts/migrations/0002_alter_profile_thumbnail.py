# Generated by Django 4.2.16 on 2024-10-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(default='images/default_thumbnail', upload_to='images'),
        ),
    ]
