# Generated by Django 5.0 on 2024-01-08 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_postcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers_counter',
        ),
    ]
