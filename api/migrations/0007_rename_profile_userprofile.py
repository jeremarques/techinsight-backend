# Generated by Django 5.0 on 2024-01-03 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
    ]
